const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let N = Number(input[0].split(" ")[0]);
let M = Number(input[0].split(" ")[1]);

let answer = [];
for (let i = 0; i < N; i++) {
  answer.push(i + 1);
}

// 역순으로 만들 바구니 가져오기.
for (let iter = 1; iter <= M; iter++) {
  // 역순으로 변경할 인덱스 의미한다.
  // a : 첫 번째 바구니 위치
  // b : 마지막 바구니 위치
  let [a, b] = input[iter].split(" ").map((n) => parseInt(n));
  // console.log(`${a} ${b}`);
  let arr = [];

  for (let j = a - 1; j < b; j++) {
    arr.push(answer[j]);
  }
  arr.reverse(); // 역순으로 변경된 바구니를 의미한다.

  // .splice(startIndex, deleteCount, add할 것 (arr 의미한다.))
  answer.splice(a - 1, b - a + 1, ...arr);
  console.log(answer);
}

console.log(answer.join(" "));
