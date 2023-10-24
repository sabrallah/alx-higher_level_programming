#!/usr/bin/node

const request = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (err) {
  console.log(err);
}

function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let y = 0; y < characters.length; ++y) {
        promises.push(getDataFrom(characters[y]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let y = 0; y < results.length; ++y) {
            console.log(JSON.parse(results[y]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

printMovieCharacters(process.argv[2]);
