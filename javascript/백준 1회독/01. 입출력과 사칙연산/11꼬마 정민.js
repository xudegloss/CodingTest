const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split(" ");

// console.log(input);
console.log(parseInt(input[0]) + parseInt(input[1]) + parseInt(input[2]));
