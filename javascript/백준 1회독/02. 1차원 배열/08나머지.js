const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);
let result = [];

for (let idx = 0; idx < input.length; idx++) {
  result.push(input[idx] % 42);
}

let answer = new Set(result);
console.log(answer.size);
