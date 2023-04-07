const { es } = require('../helpers/elastic');
const { cst } = require('../../utils/constants').default;
const logger = require('pino')()

const actionHelper = {
    getAction: async (actionId) => {
        let actionSource = await es.getDocumentByID(cst.ACTIONS, actionId);
        logger.info(actionSource);
        return actionSource;
    },
    writeAction: async (action) => {
        let indexStatus = await es.indexDocument(cst.ACTIONS, action);
        logger.info(indexStatus);
        return indexStatus;
    },
    
}


module.exports = actionHelper;