#!/usr/bin/node
const fs = require('fs');

function writeToFile(filePath, content) {
  try {
    fs.writeFileSync(filePath, content, { encoding: 'utf-8' });
    console.log('File written successfully!');
  } catch (error) {
    console.error('Error occurred while writing to file:', error);
  }
}

// Usage example
const filePath = process.argv[2]; // First command-line argument
const stringToWrite = process.argv[3]; // Second command-line argument

writeToFile(filePath, stringToWrite);
