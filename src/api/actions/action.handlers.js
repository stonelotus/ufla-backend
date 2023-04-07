const { response } = require('express');
const { es } = require('../../helpers/elastic');
const { cst } = require('../../utils/constants');
const logger = require('pino')()

const actionHandler = {
    getAction: async (actionId) => {
        let actionSource = await es.getDocumentByID(cst.ACTIONS, actionId);
        logger.info(actionSource);
        return actionSource;
    },
    writeAction: async (action) => {
        let response = await es.indexDocument(cst.ACTIONS, action);
        return response.status;
    },
    processAction: async (req, res) => {
        let actionObject = req.body;
        let status = await actionHandler.writeAction(actionObject);
        let message = (status == cst.STATUS_SUCCESS) ? "Action registered to db." : "Action could not be registered to db.";
        res.json({ message: message, status: status})
    },
    getActionsByFlowID: async(flowID) => {
        let query = {
            bool: {
                must: [
                    { match: { flowID: flowID } }
                ]
            }
        }
        let actions = await es.search(cst.ACTIONS, { flowID: flowID });
        return actions;
    }
}


module.exports = actionHandler;