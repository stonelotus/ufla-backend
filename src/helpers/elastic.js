const logger = require('pino')()
const { Client } = require("@elastic/elasticsearch");
const { cst } = require('../utils/constants');



const es = new Client({
    node: 'http://64.226.91.205:9200',
    // auth: {
    //     username: 'dio',
    //     password: 'gaby12gaby12='
    //   }
});


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
      logger.info(response);  //TODO error handling
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
      return {status: response.result == 'created' ? cst.STATUS_SUCCESS:'error'}
    } catch (error) {
      logger.error('Error indexing document:', error);
      return {status: 'error'}
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
      return response?.hits?.hits ?? 'broken'
    } catch (error) {
      logger.error('Error searching documents:', error);
    }
  },
  getDocumentByID: async (indexName, id) => {
    try {
      const response = await es.get({
        index: indexName,
        id: id
      });
      logger.info(response);
      return response._source ?? 'broken'
    } catch (error) {
      logger.error('Error getting document by ID:', error);
    }
  }
}

module.exports = {
  esTests: elasticTests,
  es:      elasticMagic
}