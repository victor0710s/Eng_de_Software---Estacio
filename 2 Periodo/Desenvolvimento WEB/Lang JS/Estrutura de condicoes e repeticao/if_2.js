/*
    Será usado a condição if + operadores logicos AND (&&) e OR (||)
    para usar o or usa-se o pipe com o atalho
    shift+alt para mudar o teclado para ingles e em seguida shift+ barra invertida \

*/

var a = 10
var b = -4

console.log("If com duas condições, onde ambas precisão ser verdadeiras.")
if (a > b && b > 0) {
    console.log("'a' é maior que 'b' e 'b' é uma numero positivo.")
}
if (a > b && b <= 0) {
    console.log("a é maior que b E b não é um número positivo");
}

console.log()

console.log("if com duas condições, onde pelo menos uma precisa ser verdadeira:");
if (a < b || b > 0) {
    console.log("a é menor que b OU b é um número positivo");
}
if (a < b || b <= 0) {
    console.log("a é menor que b OU b não é um número positivo");
}