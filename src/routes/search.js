const express = require('express');
const router = express.Router();
const {esTests, es} = require('../utils/elastic');

router.post('/create-index/:indexName', async (req, res) => {
  const indexName = req.params.indexName;
  await elasticsearchUtils.createIndex(indexName);
  res.json({ message: `Index '${indexName}' created` });
});

router.delete('/delete-index/:indexName', async (req, res) => {
  const indexName = req.params.indexName;
  await elasticsearchUtils.deleteIndex(indexName);
  res.json({ message: `Index '${indexName}' deleted` });
});

router.post('/index-document/:indexName', async (req, res) => {
  const indexName = req.params.indexName;
  const document = req.body;
  await elasticsearchUtils.indexDocument(indexName, document);
  res.json({ message: 'Document indexed' });
});

router.get('/search/:indexName/:query', async (req, res) => {
  const indexName = req.params.indexName;
  const query =  req.params.query;
  const results = await es.search(indexName, query);
  res.json(results);
});

router.get('/test/:testName', async (req, res) => {
    const testName = req.params.testName;
    switch (testName) {
        case 'sanity':
                esTests.sanityCheck();
                break;
        default:
                esTests.sanityCheck();
                break;
    }
    res.json({ message: `Test '${testName}' ran` });
});

module.exports = router;