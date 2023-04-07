const { es } = require('../../helpers/elastic')


const flowHandler = {
    getFlowFromDB: async (flowId) => {
        let flowObject = await es.getDocumentByID('flow', flowId);
        logger.info(flowObject);
        return flowObject ?? 'broken'
    },
    pushFlowToDB: async (flowObject) => {
        let flowPushStatus = await es.indexDocument('flow', flowObject);
        logger.info(flowPushStatus);
        return flowPushStatus ?? 'broken'
    }
}

module.exports = flowHandler;