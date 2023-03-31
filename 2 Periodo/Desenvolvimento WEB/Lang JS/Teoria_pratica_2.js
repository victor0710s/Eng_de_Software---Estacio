var num1 = prompt("Digite um numero inteiro e positivo: "); // Input de usuario 
var vetor = []; //criando um vetor(lista em python) vazia

/* Antriormente foi colocado const vetor,
mas por ser uma constante nao seria possivel a mudanca de seus valores
e seria ocasionado um erro de Assignment! */

while (num1 < 0) {//condicao para saber se o numero é negativo e se for ficar pedindo por um numero positivo
    alert("O numero recebido é negativo, por favor digite um numero positivo!");
    num1 = prompt("Digite um numero inteiro e positivo: ");
}
if (num1 > 0) { // se o numero recebido for positivo sera adicionado ao indice 0 do vetor 
    vetor[0] = num1;
}

var num2 = prompt("Digite outro numero inteiro e positivo: ");// Input de usuario 

while (num2 < 0) {//condicao para saber se o numero é negativo e se for ficar pedindo por um numero positivo
    alert("O numero recebido é negativo, por favor digite um numero positivo!");
    num2 = prompt("Digite um numero inteiro e positivo: ");
}
if (num2 > 0) {// se o numero recebido for positivo sera adicionado ao indice 1 do vetor 
    vetor[1] = num2;
}

console.log(vetor); // imprime o vetor no console somente para ver possiveis erros 

var div = divida(vetor) // chamando uma funcao passado o vetor como parametro
function divida(vetor) { //criacao da funcao que pega os indices 0 e 1 do vetor e os divide e retorna o resultado para a varivel div criada anteriormente
    let r = 0; // inicializacao de uma variavel de bloco, ou seja, so pode ser usada dentro da função
    r = vetor[0] / vetor[1]; // divisao dos numeros usando como referencia seus indices no vetor 
    return r; // retornando resultado da divisao
}
alert("O resultado da divisão é " + div); // gera um pop-up mostrando o resultado da divisao
