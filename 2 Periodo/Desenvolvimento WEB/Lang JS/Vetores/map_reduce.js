const numbers = [65, 44, 12, 4];

const newArr = numbers.map((x) => x * 5); // multiplica cada item por 5
console.log(newArr);

const soma = numbers.reduce((x, y) => x + y); // soma todos os pares x e y ate que fique so um valor
console.log(soma)