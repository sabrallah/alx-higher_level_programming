#!/usr/bin/node
const myVar = process.argv.length;
console.log(myVar === 2 ? 'No argument' : myVar === 3 ? 'Argument found' : 'Arguments found');
