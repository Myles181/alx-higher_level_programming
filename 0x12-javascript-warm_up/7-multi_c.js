#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);
let i;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
