const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split(" ");

let hour = Number(input[0]);
let min = Number(input[1]);

if (min < 45) {
  let remainMin = 45 - min;
  min = 60 - remainMin;
  hour = hour === 0 ? 23 : hour - 1;
  console.log(hour, min);
} else {
  // hour 줄일 필요가 전혀 없다 (해결)
  // hour = hour === 0 ? 23 : hour - 1;
  console.log(hour, min - 45);
}
