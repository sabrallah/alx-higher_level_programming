#!/usr/bin/node
function factorial (y) {
  if (y < 0) {
    return (-1);
  }
  if (y === 0 || isNaN(n)) {
    return (1);
  }
  return (y * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
