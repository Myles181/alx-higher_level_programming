#!/usr/bin/node

/**
 * Find the maximum value of the arguments passed in
 */
const args = process.argv;
let max = 0;
let i;

if (args.length > 3) {
  for (i = 2; i <= args.length; i++) {
    if (max < parseInt(args[i])) {
      max = parseInt(args[i]);
    }
  }
}
else {
  max = 0;
}
console.log(max);
