#!/usr/bin/node

const request = require('request');
const URL = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
