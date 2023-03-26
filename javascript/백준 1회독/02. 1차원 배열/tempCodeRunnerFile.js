const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");

let N = Number(input[0].split(" ")[0]);
let M = Number(input[0].split(" ")[1]);

let answer = [];
for (let i = 0; i < N; i++) {
  answer.push(i + 1);
}

for (let iter = 0; iter < M; iter++) {
  let arr = input[iter + 1].split(" ");

  if (arr[0] !== arr[1]) {
    // 구조 분해 할당 사용하기. (Swap)
    answer.slice(arr[0] - 1, arr[1]).reverse();
  }
}

console.log(answer.join(" "));
console.log(answer.slice(0, 2).reverse());
