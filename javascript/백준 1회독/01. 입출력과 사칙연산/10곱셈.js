const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");

// console.log(input);

const firstNum = parseInt(input[0]);
const secondNum = parseInt(input[1]);

// console.log(parseInt(String(secondNum)[0]));
console.log(firstNum * parseInt(String(secondNum)[2]));
console.log(firstNum * parseInt(String(secondNum)[1]));
console.log(firstNum * parseInt(String(secondNum)[0]));
console.log(firstNum * parseInt(String(secondNum)));
