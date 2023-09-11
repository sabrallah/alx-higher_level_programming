#!/usr/bin/node
console.log(typeof process.argv[2] === 'nondefined' ? 'No argument' : process.argv[2]);
