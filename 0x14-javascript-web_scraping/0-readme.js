#!/usr/bin/node

const fs = require('fs');

const file = process.argv[2];

fs.readFile(file, (err, data) => {
  if (data) {
    console.log(data.toString());
  } else {
    console.log(err);
  }
});
