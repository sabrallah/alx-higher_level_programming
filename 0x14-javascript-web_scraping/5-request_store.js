#!/usr/bin/node
const fs = require('fs');
const req = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

req.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const fileStream = fs.createWriteStream(filePath);
    fileStream.write(body);
  } else {
    console.log(err);
  }
});
