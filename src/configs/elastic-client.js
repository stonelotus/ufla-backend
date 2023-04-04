// backend/elastic-client.js
const { Client } = require("@elastic/elasticsearch");

// require("dotenv").config({ path: ".elastic.env" });

const elasticClient = new Client({
    node: 'http://64.226.91.205:9200',
    // auth: {
    //     username: 'dio',
    //     password: 'gaby12gaby12='
    //   }
});

module.exports = {
    es: elasticClient
}