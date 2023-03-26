const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");

let maxVal = parseInt(input[0]);
let maxIdx = 0;

for (let idx = 1; idx < input.length; idx++) {
  if (parseInt(input[idx]) > maxVal) {
    maxVal = parseInt(input[idx]);
    maxIdx = idx;
  }
}

console.log(maxVal);
console.log(maxIdx + 1);
