#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  process.exit(0);
}

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

/**
 * make a get request and return a promise
 */
function makeGetRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(response.statusCode);
      } else {
        // Parse the JSON response
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * main function
 */
async function main () {
  await makeGetRequest(filmUrl).then((film) => {
    const characters = film.characters;
    const promises = [];

    for (const ch of characters) {
      promises.push(makeGetRequest(ch));
    }

    Promise.all(promises).then((people) => {
      for (const person of people) {
        console.log(person.name);
      }
    });
  });
}

main();
