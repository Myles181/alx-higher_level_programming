#!/usr/bin/node

/**
 * Reads a file
 */
const file = process.argv[2];

var fs = require('fs');

fs.readFile(file, 'utf8', function (error, content) {
	console.log(error || content);
});
