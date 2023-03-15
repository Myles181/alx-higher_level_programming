#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0) {
      this.width = undefined;
    } else if (h <= 0) {
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
}
