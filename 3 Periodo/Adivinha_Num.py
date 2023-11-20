'''
Um número alvo é escolhido de 0 a N.
O usuário digita um número tentando adivinhar o mesmo, o algoritmo
recebe o input do usuário e dá dicas se o número informado é maior
ou menor do que o número de 0 a N.

Estratégia 1 - Adivinhar em ordem crescente
Estratégia 2 - Buscar em binários (Metade em Metade)
'''

import random

numero = random.randint(0, 100)

# print(numero)
print('Tente adivinhar o número de 0 a 100.')
acertou = False
while not acertou:
    user_input = int(
        input('Digite o número que você acha que é o sorteado:\nR:'))

    if user_input != numero:
        if user_input < numero:
            print('Você errouuu, mas foi quase!! Seu número é menor que o sorteado.')
        elif user_input > numero:
            print('Você errouuu, mas foi quase!! Seu número é maior que o sorteado.')

    elif user_input == numero:
        print('Parabénsss, você adivinhou o número!')
        acertou = True

    else:
        if user_input > 100 or user_input < 0:
            print('Numero invalido, somente de 0 a 100...')
