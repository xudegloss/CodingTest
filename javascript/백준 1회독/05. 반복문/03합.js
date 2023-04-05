// 3 = 1 + 2 + 3

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let n = Number(input);
let sum = 0;

for (let i = 1; i < n + 1; i++) {
  sum += i;
}

console.log(sum);
