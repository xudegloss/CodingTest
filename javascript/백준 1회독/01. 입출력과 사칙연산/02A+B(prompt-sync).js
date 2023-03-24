// const prompt = require("prompt-sync")({ sigint: true });
// 모듈 불러와서 진행하는 것이기 때문에, 백준에서 돌아가지 않는다.
const prompt = require("prompt-sync")();
let [A, B] = prompt("두 수를 입력하세요 : ").split(" ");
console.log(Number(A) + Number(B));
