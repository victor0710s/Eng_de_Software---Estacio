# Exemplo montagem de arvore binaria
# class NoArvore:
#     def __init__(self, chave=None, esquerda=None, direita=None) -> None:
#         self.chave = chave
#         self.esquerda = esquerda
#         self.direita = direita


# if __name__ == '__main__':
#     raiz = NoArvore(6)

#     raiz.esquerda = NoArvore(8)
#     raiz.direita = NoArvore(4)

#     print(raiz)


# ----------- Imprimir Arvore -----------
class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


if __name__ == '__main__':
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)

    cont = [10]

    def ImprimeArvoreRecurs(raiz, nivel):
        if raiz == None:
            nivel += cont[0]
            return nivel

        # Imprime filhos a direita
        ImprimeArvoreRecurs(raiz.direita, nivel)
        print()

        for i in range(cont[0], nivel):
            print(end=' ')
            print(f'{raiz.chave}<')

        # Imprime filhos a esquerda
        ImprimeArvoreRecurs(raiz.esquerda, nivel)

    def imprimeArvore(raiz):
        ImprimeArvoreRecurs(raiz, 0)
