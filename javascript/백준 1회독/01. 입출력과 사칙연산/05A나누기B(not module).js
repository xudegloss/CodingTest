const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split(" ");

let A = parseInt(input[0]);
let B = parseInt(input[1]);
console.log(A / B);
