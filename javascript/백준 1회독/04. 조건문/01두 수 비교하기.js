const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split(" ");

let firstNum = Number(input[0]);
let secNum = Number(input[1]);

if (firstNum > secNum) {
  console.log(">");
} else if (firstNum < secNum) {
  console.log("<");
} else {
  console.log("==");
}

// 삼항 연산자 이용하기
// 다중 삼항 연산자 이용하기 (계속 조건 붙여주면 된다.)

let answer = firstNum > secNum ? ">" : firstNum < secNum ? "<" : "==";
console.log(answer);
