const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let n = Number(input);

for (let i = 1; i < 10; i++) {
  console.log(`${n} * ${i} = ${n * i}`);
}
