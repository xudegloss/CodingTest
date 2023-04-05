const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let n = Number(input);
for (let i = 1; i < n + 1; i++) {
  // 문자열 곱하기 숫자가 불가능하니까, repeat 함수 이용하기
  console.log("*".repeat(i));
}
