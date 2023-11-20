'''
1. Pegue a carta do topo do baralho de entrada (carta atual).

2. Compare a carta atual com a carta do topo do baralho de saída:
se a da saída for maior, então coloque a carta atual no topo do baralho
de saída, senão repita o passo 2 com a próxima carta do baralho de saída.

3. Se o baralho de entrada estiver vazio, então o algoritmo acabou, 
senão repita o passo 1.

'''
import random

cartas_baralho = random.sample(range(1, 11), 10)


def ordena(baralho_principal):
    cartas_saida = []

    # Enquanto tiver cartas no baralho while recebe True
    while baralho_principal:
        carta_atual = baralho_principal.pop(0)

        # Verifica se tem carta no baralho de saida e se a ultima
        # carta é menor que a atual, se for, a mesma é removida do baralho
        # e a carta atual ocupa seu lugar.
        while cartas_saida and cartas_saida[-1] > carta_atual:
            baralho_principal.insert(0, cartas_saida.pop())

        cartas_saida.append(carta_atual)

    return cartas_saida


ordenado = ordena(cartas_baralho)

if __name__ == '__main__':
    print('TOPO')
    for i in ordenado:
        print(i, '\n')

    print('FUNDO')
