#!/usr/bin/node
const request = require('request');
const args = process.argv;
// Request URL
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}/`;

function makeReq (charUrl) {
  return new Promise((resolve, reject) => {
    request(charUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body);
  const characterPromises = data.characters.map(characterUrl => makeReq(characterUrl));
  Promise.all(characterPromises)
    .then(characters => {
      characters.map(chara => console.log(chara));
    })
    .catch(error => {
      console.log(error);
    });
});
