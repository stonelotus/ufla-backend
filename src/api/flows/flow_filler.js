
function writeComponent(component) {
    const fs = require('fs');

    jsonComponent = JSON.stringify(component);
    jsonComponent += ','

    fs.appendFile('data/flow.json', jsonComponent, err => {
      if (err) {
        console.error(err);
      }
      else {
        console.log("FLOW FILLER : File written successfully");
      }
    });

}

module.exports = {
    writeComponent: writeComponent
}
