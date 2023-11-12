#!/usr/bin/node
// prit characters of starwars movie based on movie id

const request = require('request');

const id = process.argv[2];

function getMovieCharacters (id) {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request(url, (err, resp, body) => {
    if (err) {
      return;
    }
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    characters.forEach(chaURL => {
      request(chaURL, (err, resp, body) => {
        if (err) {
          return;
        }
        const chdata = JSON.parse(body);
        console.log(chdata.name);
      });
    });
  });
}

getMovieCharacters(id);