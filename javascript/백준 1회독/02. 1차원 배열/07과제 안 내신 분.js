const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let arr = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .split("\n")
  .map(Number);

for (let i = 1; i <= 30; i++) {
  if (!arr.includes(i)) {
    console.log(i);
  }
}
