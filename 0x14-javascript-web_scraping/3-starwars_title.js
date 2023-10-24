#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
req.get(url + id, (error, res, body) => {
  if (!error && res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(error);
  }
});
