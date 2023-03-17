#!/usr/bin/node

/**
 * Find the Second maximum value of the arguments passed in
 */
const args = process.argv;
let Fmax = 0;
let Smax = 0;
let i;

if (args.length > 3) {
  /* First maximum number */
  for (i = 2; i <= args.length; i++) {
    if (Fmax < parseInt(args[i])) {
      Fmax = parseInt(args[i]);
    }
  }
  /* Second maximum number */
  for (i = 2; i <= args.length; i++) {
    if (args[i] !== Fmax) {
      if (Smax < parseInt(args[i])) {
        Smax = parseInt(args[i]);
      }
    }
  }
  console.log(Smax);
} else {
  console.log(0);
}
