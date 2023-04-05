const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let iter = Number(input[0]);
for (let i = 1; i < iter + 1; i++) {
  let A = Number(input[i][0]);
  let B = Number(input[i][2]); // 2라는 사실 주의하기.
  console.log(A + B);
}
