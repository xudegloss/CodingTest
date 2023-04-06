const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";

let input = fs
  .readFileSync(__dirname + filePath)
  .toString()
  .trim();

let locationObj = {
  a: 0,
  b: 1,
  c: 2,
  d: 3,
  e: 4,
  f: 5,
  g: 6,
  h: 7,
  i: 8,
  j: 9,
  k: 10,
  l: 11,
  m: 12,
  n: 13,
  o: 14,
  p: 15,
  q: 16,
  r: 17,
  s: 18,
  t: 19,
  u: 20,
  v: 21,
  w: 22,
  x: 23,
  y: 24,
  z: 25,
};

let objectKeys = Object.keys(locationObj).join("");
let answer = [];

for (let i = 0; i < objectKeys.length; i++) {
  answer.push(-1);
}

for (let i = 0; i < input.length; i++) {
  // 만약에 숫자가 있는 경우, 그냥 반복문 넘어가기
  if (answer[locationObj[input[i]]] !== -1) {
    continue;
  }
  answer[locationObj[input[i]]] = i;
}

console.log(answer.join(" "));
