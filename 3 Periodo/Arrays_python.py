# Usaremos listas em python como exemplo do array

# ------------------------ Lista base ------------------------
# lista_nomes = ['Victor', 'Luiza', 'Zayra']
# print(lista_nomes)
# lista_nomes.append('Mayra')
# print(lista_nomes)
# lista_nomes.remove('Victor')
# print(lista_nomes)
# lista_nomes.pop(0) #Remove o item de acordo com a indice
# print(lista_nomes)

# ------------------------ Lista com Numpy ------------------------
import numpy as np

nomes = np.array(['Victor', 'Luiza', 'Zayra'])
print(nomes)
copia = nomes.copy()
copia[0] = 'Nelson'  # Altera o elemento de acordo com o indice
print(nomes)
print(copia)
visao = nomes.view()
visao[0] = 'Fulano'
print(nomes)
print(visao)

for indice, valor in enumerate(nomes):
    print(indice, valor)
