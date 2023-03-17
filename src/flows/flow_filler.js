

function writeComponent(name) {
    const fs = require('fs');

    const content = name + '\n';
    fs.appendFile('data/file.txt', content, err => {
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


