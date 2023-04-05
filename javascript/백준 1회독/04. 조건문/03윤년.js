const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let year = Number(input);

// if (year % 4 === 0 && year % 100 !== 0) {
//   console.log(1);
// } else if (year % 400 === 0) {
//   console.log(1);
// } else {
//   console.log(0);
// }

// 삼항 다중 연산자 이용하기

let answer = year % 4 === 0 && year % 100 !== 0 ? 1 : year % 400 === 0 ? 1 : 0;
console.log(answer);
