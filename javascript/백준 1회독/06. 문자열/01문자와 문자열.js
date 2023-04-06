const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let string = String(input[0]);
let order = Number(input[1]);

// length-1이 아닌 length로 접근해야 한다
// if n=5, idx로 접근해야하기 때문에 4가 되는 지점을 찾아야 한다.

for (let i = 0; i < string.length; i++) {
  if (i === order - 1) {
    console.log(string[i]);
  }
}
