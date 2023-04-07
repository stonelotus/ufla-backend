const { es } = require('../../helpers/elastic')
const actionHandler  = require('../actions/action.handlers')
const { cst }  = require('../../utils/constants')
const logger = require('pino')()

const flowHandler = {
    getFlowFromDB: async (flowId) => {
        let flowObject = await es.getDocumentByID(cst.FLOWS, flowId);
        return flowObject ?? 'error'
    },
    pushFlowToDB: async (flowObject) => {
        let flowPushStatus = await es.indexDocument(cst.FLOWS, flowObject);
        return flowPushStatus ?? 'error'
    },
    createFlow: async (flowID) => {
        let actions = await actionHandler.getActionsByFlowID(flowID);
        logger.debug(actions);
        let flowObject = {
            flowID: flowID,
            actions: actions,
            timeStamp: new Date().toISOString()
        }
        let flowPushStatus = await flowHandler.pushFlowToDB(flowObject);

        return flowPushStatus;
    },
    finishFlow: async (req, res) => {
        let flowID = req.query.flowID;
        let flowPushStatus = await flowHandler.createFlow(flowID);
        message = (flowPushStatus.status == cst.STATUS_SUCCESS) ? "Flow registered to db." : "Flow could not be registered to db.";
        res.json({ message: message, status: flowPushStatus})
    }
}

module.exports = flowHandler;