#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + id, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const chara = data.characters;
    for (const per of chara) {
      request.get(per, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
      });
    }
  } else {
    console.log(err);
  }
});
