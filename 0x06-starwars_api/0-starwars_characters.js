#!/usr/bin/node
// prit characters of starwars movie based on movie id

const request = require('request');

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

// Check if a movie ID is provided as a command-line argument
const movieId = process.argv[2];
if (!movieId) {
  process.exit(1);
}

// Call the function with the provided movie ID
getMovieCharacters(movieId);
