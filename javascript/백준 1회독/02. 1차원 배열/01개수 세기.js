const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n");

// console.log(input[1].split(" ").length); // 11
result = 0;
for (let i = 0; i < input[1].split(" ").length; i++) {
  if (input[2] === input[1].split(" ")[i]) {
    result += 1;
  }
}

console.log(result);
