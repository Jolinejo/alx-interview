#!/usr/bin/node
const request = require('request');
const args = process.argv;
// Request URL
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}/`;

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // Printing status code
  // Printing body
  const data = JSON.parse(body);
  for (let i = 0; i < data.characters.length; i++) {
    const url2 = data.characters[i];
    request(url2, (error, response, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});
