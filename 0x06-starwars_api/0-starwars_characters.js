#!/usr/bin/node
// prit characters of starwars movie based on movie id

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, resp, body) => {
  if (err) {
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  printCha(characters, 0);
});

function printCha (ch, indx) {
  request(ch[indx], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (indx + 1 < ch.length) {
        printCha(ch, indx + 1);
      }
    }
  });
}
