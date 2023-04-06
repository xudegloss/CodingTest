const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split(" ");

// 빈칸인 경우 length가 1로 나오기 때문에 그 부분만 예외 처리하기
input[0] === "" ? console.log(0) : console.log(input.length);
