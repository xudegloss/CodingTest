const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let N = Number(input[0]);
let arr = input[1].split(" ").map(Number);

// Math.max.apply(null, arr);
let max = Math.max.apply(null, arr);
let new_arr = [];

for (let i = 0; i < arr.length; i++) {
  new_arr.push((arr[i] / max) * 100);
}

// reduce 함수로 합계 구하기.
const arr_sum = new_arr.reduce(function add(init, currValue) {
  return init + currValue;
}, 0);

console.log(arr_sum / N);
