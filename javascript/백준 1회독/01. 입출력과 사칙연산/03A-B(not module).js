// 1. commonJS Modules 불러오기.
const fs = require("fs");

// 2. 파일 경로를 리눅스인 경우에는 /dev/stdin 실행하고, 윈도우인 경우에는 /input.txt 가져오기.
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

// 3. readFileSync를 통하여 input 가져오기.
let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split(" ");

console.log(input);

// 4. 원하는 연산 진행하기.
let A = parseInt(input[0]);
let B = parseInt(input[1]);
console.log(A - B);
