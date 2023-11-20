# Ordenação de array pelo metodo Bubble Sort onde o algoritmo passa pela lista
# até que a mesma esteja ordenada, encerrando assim o algoritmo.


def trocar(seq, i):
    aux = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = aux


seq = [0, 23, 1, 5, 43, 7, 8, 66, 65]
troca = 1

while troca:
    troca = 0
    i = 0

    for i in range(len(seq)-1):
        if seq[i] > seq[i + 1]:
            trocar(seq, i)
            troca = 1

print(seq)
