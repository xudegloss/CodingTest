const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let iter = Number(input[0]);
for (let i = 1; i < iter + 1; i++) {
  let A = Number(input[i].split(" ")[0]);
  let B = Number(input[i].split(" ")[1]);
  console.log(`Case #${i}: ${A} + ${B} = ${A + B}`);
}
