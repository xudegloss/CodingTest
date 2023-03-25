let a = "제 1회";
console.log(Number(a)); // NaN
console.log(parseInt(a)); // NaN

let b = "2023년";
console.log(Number(b)); // NaN
console.log(parseInt(b)); // 2023

let c = "2023";
console.log(Number(c)); // 2023
console.log(parseInt(c)); // 2023

let d = "123.45678";
console.log(Number(d)); // 123.45678
console.log(parseInt(d)); // 123
console.log(parseFloat(d)); // 123.45678
