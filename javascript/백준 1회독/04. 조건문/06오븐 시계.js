// 1. 60분 넘지 않으면 그냥 더해주기.
// 2. 60분 넘으면 시간 더하고, 나머지 만큼 분에 넣어주기.
// 3. 만약에 23시 넘으면, 그 시간을 24으로 나눈 나머지를 시간에 넣어주기.
// 2번 3번 조건을 한꺼번에 지정하기.

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim()
  .split("\n");

let hour = Number(input[0].split(" ")[0]);
let min = Number(input[0].split(" ")[1]);
let plusMin = Number(input[1]);

if (min + plusMin < 60) {
  min += plusMin;
  console.log(hour % 24, min);
} else {
  let plusHour = (min + plusMin) / 60;
  // 몫 구하는 법 : parseInt 넣어주기.
  hour += parseInt(plusHour);
  min = (min + plusMin) % 60;
  console.log(hour % 24, min);
}
