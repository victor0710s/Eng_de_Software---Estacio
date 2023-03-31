var a = 5;
var b = -1;
var c = false; // valores possíveis -> True, False

console.log("if com mais de duas condições e combinação de && c ||:");
if ((a > b && b > 0) || (a > b && b <= 0)) {
    console.log("a é maior que b E b é um número positivo");
    console.log("OU");
    console.log("a é maior que b E b não é um número positivo");
}
console.log()
console.log("if com condição não verdadeira:");
if (!c) {
    console.log("c tem valor false");
}