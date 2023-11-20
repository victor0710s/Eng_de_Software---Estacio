# Aplicando exemplos de recursao em casos simples

# Fatorial
# def fatorial(n):
#     if n == 1 or n == 0: # O(n)
#         return 1
#     else:
#         return n * fatorial(n - 1)


# numero = 5 # O(1)
# resultado = fatorial(numero)

# print(f'O fatorial de {numero} é {resultado}')

# Complexidade -> O(n) , ou seja, aumenta conforme o numero de entradas


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # O(n)


termo = 10  # O(1)
resultado = fibonacci(termo)

print(f'O termo {termo} da sequencia de Fibonacci é {resultado}')


# Complexidade -> O(2^n), pois a função se chama 2 vezes
