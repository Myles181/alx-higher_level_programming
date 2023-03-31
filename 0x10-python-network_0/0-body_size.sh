#!/usr/bin/bash
#Take in a URL and display the size in bytes

if [ $# -eq 0 ]; then
	echo "Usage: $0 URL"
else
	curl -s $1 | wc -c
fi
