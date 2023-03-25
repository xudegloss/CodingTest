const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

// 문자열 정보인 경우에는 인코딩 처리하기.
let input = fs
  .readFileSync(__dirname + filePath, "utf-8")
  .toString()
  .trim();

// 문자 하나만 입력받는 경우

console.log(input + "??!");
console.log(`${input}??!`);

const special = "??!";
process.stdout.write(input);
process.stdout.write(special);
