const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

// console.log(input[0].split(" ").map(Number));
let N = input[0].split(" ").map(Number)[0]; // 5
let M = input[0].split(" ").map(Number)[1]; // 4
// console.log(`${N} ${M}`);
let obj = {};

for (let i = 0; i < N; i++) {
  obj[i + 1] = [0];
}

for (let idx = 1; idx <= M; idx++) {
  let arr = input[idx].split(" ");
  let firstBox = arr[0];
  let lastBox = arr[1];
  let ball = arr[2];

  for (let i = firstBox; i <= lastBox; i++) {
    let len = Object.values(obj[i]).length;

    if (len === 0) {
      obj[i].push(ball);
    } else {
      obj[i].pop();
      obj[i].push(ball);
    }
  }
}

console.log(Object.values(obj).map(Number).join(" "));
