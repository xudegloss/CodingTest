const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let score = Number(input);

let answer =
  score >= 90
    ? "A"
    : score >= 80
    ? "B"
    : score >= 70
    ? "C"
    : score >= 60
    ? "D"
    : "F";

console.log(answer);

// const answer =
//   90 <= score && score <= 100
//     ? "A"
//     : 80 <= score && score <= 89
//     ? "B"
//     : 70 <= score && score <= 79
//     ? "C"
//     : 60 <= score && score <= 69
//     ? "D"
//     : "F";

// console.log(answer);
