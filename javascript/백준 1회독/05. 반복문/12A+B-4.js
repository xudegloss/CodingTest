const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let n = input.length;
for (let idx = 0; idx < n; idx++) {
  let A = Number(input[idx].split(" ")[0]);
  let B = Number(input[idx].split(" ")[1]);
  console.log(A + B);
}
