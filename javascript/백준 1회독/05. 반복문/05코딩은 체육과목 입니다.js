const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let n = Number(input);
let iter = parseInt(n / 4); // 5
answer = "";

// iter로 이용하기 (반복 횟수)

for (let i = 0; i <= iter; i++) {
  if (i !== iter) {
    answer += "long ";
  } else {
    answer += "int";
  }
}

console.log(answer);
