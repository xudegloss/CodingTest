const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let x = Number(input[0]);
let n = Number(input[1]);
let sum = 0;

for (let idx = 2; idx < n + 2; idx++) {
  let a = Number(input[idx].split(" ")[0]);
  let b = Number(input[idx].split(" ")[1]);
  sum += a * b;
}

if (sum === x) {
  console.log("Yes");
} else {
  console.log("No");
}
