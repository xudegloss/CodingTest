const fs = require("fs");

// readFileSync을 0으로 지정하면 문제가 해결된다.
const input = fs.readFileSync(0).toString().trim().split("\n");
let x = Number(input[0]);
let y = Number(input[1]);

if (x > 0) {
  if (y > 0) {
    console.log(1);
  } else {
    console.log(4);
  }
} else {
  if (y > 0) {
    console.log(2);
  } else {
    console.log(3);
  }
}
