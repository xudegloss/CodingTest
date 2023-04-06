const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split(" ");

let firstNum = Number(input[0].split("").reverse().join(""));
let secNum = Number(input[1].split("").reverse().join(""));

if (firstNum < secNum) {
  console.log(secNum);
} else {
  console.log(firstNum);
}
