'''
--- 3 passos para calcular a complexidade: ---

1 - Levar em consideração apenas as repetições do código

2 - Verificar a complexidade das funções/metódos próprios da
linguagem (se utilizada)

3- Ignorar as constantes e utilizar o termo de maior grau

'''
# -----------------------------------------------------------------------

# Function 1


def func1(n):
    soma = 0  # O(1)
    for i in range(n + 1):  # O(n), n = quantity of inputs
        soma += i

    return soma  # O(1)


# Function 2
def func2(n):
    return (n * (n + 1)) / 2  # O(1), constant


# Function 3
def func3(n):
    tamanho = len(n)  # O(1)
    for i in range(0, tamanho):  # O(n)
        for j in range(0, tamanho):  # O(n)
            if i != j or n[i] == n[j]:  # O(1)
                return True  # O(1)

    return False  # O(1)


# Function 4
def func4(n, m):
    tamanho = len(n)  # O(1)
    tamanho2 = len(m)  # O(1)
    for i in range(0, tamanho):  # O(n)
        for j in range(0, tamanho2):  # O(m)
            if n[i] == n[j]:  # O(1)
                return True  # O(1)

    return False  # O(1)


# Function 5
def func5(idades):
    tamanho = len(idades)  # O(1)
    menor_idade = 200  # O(1)
    for i in range(0, tamanho):  # O(n)
        if idades[i] < menor_idade:  # O(1)
            menor_idade = idades[i]  # O(1)
    cont = 0  # O(1)
    for i in range(0, tamanho):  # O(n)
        if idades[i] == menor_idade:  # O(1)
            cont += 1  # O(1)

    return cont > 1  # O(1)


# Function 6
def func6(idades):
    sorted(idades)
    return idades[0] == idades[1]


# Function 7
def merge_sort(n):
    if len(n) <= 1:
        return n

    middle = len(n) // 2
    left = n[:middle]
    right = n[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


def func7(n, m):
    n_sorted = merge_sort(n)
    m_sorted = merge_sort(list(m))

    i, j = 0, 0

    while i < len(n_sorted) and j < len(m_sorted):
        if n_sorted[i] == m_sorted[j]:
            return True
        elif n_sorted[i] < m_sorted[j]:
            i += 1
        else:
            j += 1

    return False


# -----------------------------------------------------------------------


'''
Function 1 -> 11 passos e conforme aumenta as entradas mais passos existirão
logo a complexidade desse codigo é O(n) [linear], n é a quantidade de passos.

Function 2 -> 3 passos e independente da quantidade de entradas será 
somente 3 passos, logo a complexidade desse codigo é O(3) [constante].

Function 3 -> Por ter 2 loops dependentes entre si, logo a complexidade
desse codigo é O(n²) [quadratica]

Function 4 -> Apesar de ter 2 loops dependentes entre si, os mesmos
recebem dois inputs diferente (tamanho e tamanho 2), logo a complexidade
desse codigo é O(n) * O(m), ou melhor O(n * m)

Function 5 -> Dentro dessa função temos 2 loops independentes, logo 
a complexidade desse codigo será O(n)

Function 6 -> Apesar de fazer a mesma coisa que a func5 e ter menos linhas
de codigo, o mesmo não é menos complexo pois utiliza um metodo/função inbutida
da linguagem python [sort()] e a mesma tem complexidade O(NlogN), logo
a complexidade desse codigo é O(NlogN)

Function 7 -> O(NlogN)
'''
