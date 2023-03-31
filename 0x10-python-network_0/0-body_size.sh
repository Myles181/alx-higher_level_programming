#!/bin/bash
#Take in a URL and display the size in bytes
curl -s "$1" | wc -c
