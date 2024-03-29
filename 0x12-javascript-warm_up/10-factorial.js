#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0 || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const args = process.argv;
const n = parseInt(args[2]);
console.log(factorial(n));
