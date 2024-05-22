#!/usr/bin/node
const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
