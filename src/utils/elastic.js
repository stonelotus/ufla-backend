const { es } = require('../configs/elastic-client');
test = async () => {
    const result = await es.search({
        index: 'tests',
        query: {
            match: { status: 'alive' }
        }
    })
}
async function searchDocuments(index, query) {
  try {
    var response = await es.search({
      index,
      body: {
        query: {
          match: { status: 'alive' }
        }
      }
    });
    console.log("pula")
    console.log(response.hits.hits);
    return response.hits.hits;
  } catch (error) {
    console.error('Error searching documents:', error);
  }
}

searchDocuments("tests", "sane_as_fk");
// test();