const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");

let num = parseInt(input[0].split(" ")[1]); // 5
let answer = [];
let arr = input[1].split(" ");

for (let i = 0; i < arr.length; i++) {
  if (arr[i] < num) {
    answer.push(arr[i]);
  }
}

// 한 줄에 모두 적으려고 하지 말고 리스트에 담은 후에 join 이용하기.
// 시간 초과 뜬다.
console.log(answer.join(" "));
