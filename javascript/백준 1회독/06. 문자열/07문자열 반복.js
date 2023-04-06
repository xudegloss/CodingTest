const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let answer = "";
const iter = Number(input[0]);

for (let i = 1; i < iter + 1; i++) {
  let repeat = Number(input[i].split(" ")[0]);
  let string = input[i].split(" ")[1];
  answer = ""; // reset 과정 필요하다

  for (let idx = 0; idx < string.length; idx++) {
    answer += string[idx].repeat(repeat);
  }
  console.log(answer);
}
