#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(parseInt(arg))) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
