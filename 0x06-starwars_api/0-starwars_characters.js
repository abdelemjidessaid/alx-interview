#!/usr/bin/node
const request = require('request');

const args = process.argv;

async function fetchCharacter (url) {
  /**
   * function that return new promise that fetch the character name
   * url: the character url
   *
   * Return: the character name
   */
  return new Promise((resolve) => {
    request.get(url, async (error, response, body) => {
      if (response && response.statusCode === 200) {
        const data = await JSON.parse(body);
        resolve(data.name);
      } else {
        console.error(error);
      }
    });
  });
}

function main () {
  /**
   * main function - entery point of program
   * fetches the film by the given id
   */
  if (args.length === 3) {
    const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}/`;
    request.get(url, async (error, response, body) => {
      // the response function
      if (response && response.statusCode === 200) {
        const data = JSON.parse(body);
        const characters = data.characters;
        for (let i = 0; i < characters.length; i++) {
          const name = await fetchCharacter(characters[i]);
          console.log(name);
        }
      } else {
        console.error('Error:', error);
      }
    });
  } else {
    console.log('Usage: node 0-starwars_characters.js <film_id>');
  }
}

main();
