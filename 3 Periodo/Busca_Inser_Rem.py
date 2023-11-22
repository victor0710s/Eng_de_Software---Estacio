# Busca, Inserção e Remoção em alocação contígua


# --------------- Codigo de Busca ---------------

# nomes = ['Joao', 'Maria', 'Ana']
# i = nomes.index('Joao')
# print(i)

# ================================================================

# def busca(k, Lista, n):
#     i = 0
#     indiceLista = -1  # Inicializa o índice como -1 (não encontrado)

#     while i < n:  # Percorre a lista até o tamanho n
#         if Lista[i] == k:  # Verifica se o elemento na posição i é igual a k
#             # Se encontrado, atualiza o índice para a posição onde o elemento foi encontrado
#             indiceLista = i
#             i = n + 1  # Interrompe o loop ao atribuir um valor que faz a condição do while ser falsa

#         i += 1  # Incrementa o contador para avançar para o próximo elemento na lista
#     # Retorna o índice onde o elemento foi encontrado ou -1 se não encontrado
#     return indiceLista


# --------------- Codigo de Inserção ---------------

# nomes = ['Victor', 'Ana', 'Luna']
# nomes.append('Maya')
# print(nomes)

# ================================================================

# def InsereL(k, Lista, n):  # Chave, Lista, Len(Lista)
#     Lista.append('')  # Adiciona o elemento a lista
#     Lista[n] = k  # O elemento n na lista passa a ter o valor de k
#     n += 1  # Incrementa o valor de n, aumentando o tamanho da lista

# ================================================================

# def InsereOrdenada(k, Lista, n):  # Chave, Lista, Len(Lista)
#     i = 0
#     posInsercao = -1

#     while i < n:
#         if Lista[i] >= k:  # Verifica se o elemento na posição i é maior ou igual à chave k
#             # Se o elemento na posição i for igual a k, retorna -1 (elemento já existe na lista)
#             if Lista[i] == k:
#                 return -1
#             else:  # Se o elemento na posição i for maior que k, encontramos o local de inserção
#                 posInsercao = i
#                 i = n + 1  # Para sair do loop, atribui um valor que faz a condição do while ser falsa
#         else:
#             i += 1  # Avança para a próxima posição na lista

#         if Lista[i] == n:  # Verifica se o elemento na posição i é igual ao tamanho da lista
#             posInsercao = n  # Se sim, a posição de inserção é no final da lista

#     Lista.append('')  # Adiciona um elemento vazio no final da lista
#     i = n  # Define i como o tamanho atual da lista
#     while i > posInsercao:  # Move os elementos para abrir espaço para a inserção
#         Lista[i] = Lista[i - 1]
#         i -= 1
#     Lista[posInsercao] = k  # Insere o elemento k na posição correta

#     return posInsercao  # Retorna a posição de inserção do elemento na lista


# --------------- Codigo de Inserção ---------------

# nomes = ['Ana', 'Gabriel', 'Maria', 'Joao']
# print(nomes)
# nomes.remove('Maria')
# print(nomes)
# nomes.pop()
# print(nomes)

# ================================================================

def Remove(k, Lista, n):
    i = 0
    posRemocao = -1

    while i < n:
        if Lista[i] == k:  # Verifica se o elemento na posição i é igual a k
            posRemocao = i  # Se for encontrado, armazena a posição para remoção
            i = n + 1  # Interrompe o loop ao atribuir um valor que faz a condição do while ser falsa
        else:
            i += 1  # Avança para a próxima posição na lista

    # Se o loop terminou sem encontrar o elemento, retorna -1 (elemento não encontrado)
    if i == n:
        return -1

    i = posRemocao
    while i < n - 1:  # Move os elementos para preencher o espaço da remoção
        Lista[i] = Lista[i + 1]
        i += 1

    # Remove o último elemento da lista (o que ficou duplicado após a movimentação)
    Lista.pop(n - 1)
    return posRemocao  # Retorna a posição do elemento removido na lista
