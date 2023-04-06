const { es } = require('../configs/elastic-client');
const logger = require('pino')()

const elasticTests = {
  sanityCheck: async () => {
    try {
      const response = await es.ping();
      logger.info(response);
    } catch (error) {
      logger.error('Error pinging Elastic:', error);
    }
  },
  searchCheck: async () => {
    try {
      const response = await es.search({
        index: 'tests',
        query: {
          match: { status: 'alive' }
        }
      });
      let statusObject = response?.hits?.hits?.[0]?._source;
      logger.info(statusObject);
      return statusObject ?? 'broken'
      
    } catch (error) {
      logger.error('Error searching documents:', error);
    }
  }
}

const elasticMagic = { 
  createIndex: async (indexName) => {
    try {
      const response = await es.indices.create({
        index: indexName
      });
      logger.info(response);
    } catch (error) {
      logger.error('Error creating index:', error);
    }
  },
  indexDocument: async (indexName, document) => {
    try {
      const response = await es.index({
        index: indexName,
        body: document
      });
      logger.info(response);
      
    } catch (error) {
      logger.error('Error indexing document:', error);
    }
  },
  search: async (indexName, query) => {
    try {
      const response = await es.search({
        index: indexName,
        body: {
          query: {
            match: query
          }
        }
      });
      logger.info(response);
      return response?.hits?.hits ?? 'broken'
    } catch (error) {
      logger.error('Error searching documents:', error);
    }
  }
}

module.exports = {
  esTests: elasticTests,
  es:      elasticMagic
}