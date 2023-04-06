// 이해 안됨...

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

for (let i = 1; i <= Number(input[0]); i++) {
  console.log(
    input[i].substring(0, 1) +
      input[i].substring(input[i].length - 1, input[i].length)
  );
}
