const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

// charPointAt, charCodeAt, charAt : 모두 비슷한 것 같다.

console.log(input.codePointAt(0));
