#!/usr/bin/node
const ifs = require('fs');
const argv = process.argv;

const filea = ifs.readFileSync(argv[2], 'utf-8').toString();
const fileb = ifs.readFileSync(argv[3], 'utf-8').toString();
ifs.writeFileSync(argv[4], filea + fileb);
