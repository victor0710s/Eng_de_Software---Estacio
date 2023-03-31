const numbers = [45, 23, 67, 1];
let txt = "";
for (let x in numbers) {
    txt += numbers[x];
}
console.log(txt)

const letters = ["J", "a", "v", "a", "S", "c", "r", "i", "p", "t"];
let txt2 = "";
for (const x of letters) {
    txt2 += x;
}
console.log(txt2)