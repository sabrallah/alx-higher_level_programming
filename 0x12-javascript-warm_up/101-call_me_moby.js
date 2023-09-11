#!/usr/bin/node
// this is my own code.
exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};
