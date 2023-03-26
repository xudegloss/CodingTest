const fs = require("fs");
const [NnM, ...exes] = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .trim()
  .split("\n");
const [n, m] = NnM.split(" ").map((e) => +e);
const baskets = new Array(n).fill(0);
let result = "";

const execute = (str) => {
  const [i, j, ball] = str.split(" ").map((e) => +e);

  for (let x = i; x <= j; x++) {
    baskets[x - 1] = ball;
  }
};

exes.forEach(execute);
baskets.forEach((e) => (result += `${e} `));
console.log(result);
