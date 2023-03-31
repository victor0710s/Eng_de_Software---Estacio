//new Date().getDay() retorna o dia da semana (0, 2,..., 6)
var num_dia = new Date().getDay();

switch (num_dia) {
    case 0:
        dia = "Domingo";
        break;
    case 1:
        dia = "Segunda-feira";
        break;
    case 2:
        dia = "Terça-feira";
        break;
    case 3:
        dia = "Quarta-feira";
        break;
    case 4:
        dia = "Quinta-feira";
        break;
    case 5:
        dia = "Sexta-feira";
        break;
    case 6:
        dia = "Sabádo";
        break;
    default:
        console.log("Dia da semana inexistente!")
        break;

}
console.log("O dia da semana é:", dia);
// mais exemplos de como usar o switch: https://www.devmedia.com.br/javascript-switch/39761