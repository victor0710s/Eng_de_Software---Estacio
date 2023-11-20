# Exemplos de matriz, ou também chamado de vetor de vetores

# ------------ Matriz Base ------------
# alimentos = [['Arroz', 6], ['Feijão', 5, 1], ['Batata', 9, 3]]
# print(alimentos)
# alimentos[0].append(2)
# print(alimentos)
# alimentos.remove(['Batata', 9, 3])
# print(alimentos)
# alimentos.pop(1)
# print(alimentos)


# ------------ Matriz com Numpy ------------
import numpy as np
numeros = np.array([[1, 23, 5], [26, 234, 163], [334, 765, 2]])
print(numeros)
minimo = numeros.min()
maximo = numeros.max()
soma = numeros.sum()
media = numeros.mean()
desvio = numeros.std()
print('Minimo:', minimo)
print('Maximo:', maximo)
print('Soma:', soma)
print('Media:', media)
print('Desvio:', desvio)
