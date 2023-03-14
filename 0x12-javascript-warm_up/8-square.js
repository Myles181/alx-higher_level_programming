#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);
let i, j, row;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    row = '';
    for (j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
