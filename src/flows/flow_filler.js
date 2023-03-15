

function writeComponent(name) {
    const fs = require('fs');

    const content = name + '\n';
    fs.appendFile('file.txt', content, err => {
      if (err) {
        console.error(err);
      }
      else {
        console.log("File written successfully");
      }
    });
}

module.exports = {
    writeComponent: writeComponent
}


