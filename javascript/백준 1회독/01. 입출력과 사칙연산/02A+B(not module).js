// commonJS Modules 불러오기.
const fs = require("fs");

// 프로그램을 실행하고 있는 디렉토리 확인하기.
console.log(process.cwd());
console.log(__dirname);

// 리눅스인 경우에는 /dev/stdin (예시 : 백준인 경우)
// 윈도우인 경우에는 /input.txt
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split(" ");

let A = parseInt(input[0]);
let B = parseInt(input[1]);
console.log(A + B);
