const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split(" ");

let firstDiceEye = Number(input[0]);
let secDiceEye = Number(input[1]);
let thiDiceEye = Number(input[2]);
let answer = 0;

// 조건 나눠서 계산해주기.

if (firstDiceEye === secDiceEye && secDiceEye === thiDiceEye) {
  answer = 10000 + firstDiceEye * 1000;
  console.log(answer);
} else if (firstDiceEye === secDiceEye || firstDiceEye === thiDiceEye) {
  answer = 1000 + firstDiceEye * 100;
  console.log(answer);
} else if (secDiceEye === thiDiceEye) {
  answer = 1000 + secDiceEye * 100;
  console.log(answer);
} else {
  answer = Math.max(firstDiceEye, secDiceEye, thiDiceEye) * 100;
  console.log(answer);
}
