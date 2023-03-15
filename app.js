const express = require('express')
const cors = require('cors')
const app = express()
const port = 3000
const bodyParser = require('body-parser');
const flowFiller = require('./src/flows/flow_filler');


const corsOpts = {
    origin: '*',
  
    methods: [
      'GET',
      'POST',
    ],
  
    allowedHeaders: [
      'Content-Type',
    ],
  };
  

app.use(cors(corsOpts));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    console.log("works from here");
    res.send('Hello World!')
})

app.post('/test', (req, res) => {
    console.log("brooo");
    console.log(req.body.name);
    flowFiller.writeComponent(req.body.name);
    res.send('Hello World!')
})
app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
    console.log("works bro");
})