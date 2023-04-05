const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let n = Number(input);
let iter = parseInt(n / 4); // 5

for (let i = 0; i < iter; i++) {
  console.log("long");
  if(i===iter){
    console.log("int")
  }
}
