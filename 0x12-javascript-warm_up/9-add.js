#!/usr/bin/node
// this the code that sum two number.

function add(a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
