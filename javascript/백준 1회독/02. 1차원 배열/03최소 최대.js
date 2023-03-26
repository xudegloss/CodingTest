const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");
let n = parseInt(input[0]);
let array = input[1].split(" ").map(Number);

// console.log(input);
let _min = input[1].split(" ")[0];
let _max = input[1].split(" ")[0];

for (let idx = 1; idx < n; idx++) {
  if (_min > array[idx]) {
    _min = array[idx];
  }

  if (_max < array[idx]) {
    _max = array[idx];
  }
}

console.log(_min, _max);
