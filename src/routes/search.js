const express = require('express');
const router = express.Router();
const {esTests, es} = require('../helpers/elastic');

router.get('/create-index/:indexName', async (req, res) => {
  const indexName = req.params.indexName;
  await es.createIndex(indexName);
  res.json({ message: `Index '${indexName}' created` });
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