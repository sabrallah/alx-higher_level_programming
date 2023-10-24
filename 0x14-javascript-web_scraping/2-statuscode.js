#!/usr/bin/node
const req = require('request');

const url = process.argv[2];

req.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
