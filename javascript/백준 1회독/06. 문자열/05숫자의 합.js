const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let sum = 0;
const iter = Number(input[0]);
for (let i = 0; i < iter; i++) {
  sum += Number(input[1][i]);
}

console.log(sum);
