#!/usr/bin/node

const request = require("request");

if (process.argv.length < 2) {
  process.exit(1);
}

const filmId = process.argv[1];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

function make_Get_Request(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      // Printing the error if occurred
      if (error) reject(error);
      else resolve(body);
    });
  });
}

make_Get_Request(filmUrl).then((film) => {
  const characters = film.characters;
  let promises = [];
  for (let char of characters) {
    promises.push(make_Get_Request(char));
  }
  let results = Promise.all(promises);
  console.log(results);
});
