let fs = require("fs");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let n = Number(input[0]);
let array = input[1].split(" ").map(Number);
// console.log(array);

let max = -1000001;
let min = 1000001;

for (let i = 0; i < n; i++) {
  if (min > array[i]) min = array[i];
  if (max < array[i]) max = array[i];
}

console.log(`${min} ${max}`);
