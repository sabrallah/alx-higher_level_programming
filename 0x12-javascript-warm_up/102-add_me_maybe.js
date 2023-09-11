#!/usr/bin/node
// this the code that log addMeMaybe.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
