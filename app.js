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
    console.log("Received action \"" + req.body.eventData.type + "\" from frontend.");
    flowFiller.writeComponent(req.body.eventData);
    res.json({
        message: "Click registered to file."
    });
})

app.listen(port, () => {
    console.log(`App listening on port ${port}`)
})