# Busca, Inserção e Remoção em alocação encadeada


# --------------- Codigo de Busca ---------------

def busca(self, k):
    noAtual = self.cabeca
    if noAtual.chave == k:
        return noAtual
    while noAtual.proximo != None:  # O(n)
        noAtual = noAtual.proximo  # Passa para o proximo no

        if noAtual.chave == k:
            return noAtual  # Chave encontrada

    return None  # Chave nao encontrada

# --------------- Codigo de Inserção ---------------


def InsereInicio(self, novoNo):
    novoNo.proximo = self.cabeca
    self.cabeca = novoNo


def InsereFinal(self, novoNo):
    noAtual = self.cabeca

    if noAtual:
        while noAtual.proximo:
            noAtual = noAtual.proximo

        noAtual.proximo = novoNo

    else:
        self.cabeca = novoNo

# Complexidade geral = O(1), mas se ordenada O(n)


# --------------- Codigo de Remoção ---------------

def RemoveLista(self, k):
    noAtual = self.cabeca
    if noAtual == None:
        return None

    if noAtual.chave == k:
        self.cabeca = noAtual.proximo
        return 0

    noAnterior = noAtual
    noAtual = noAtual.proximo

    while noAtual != None:
        if noAtual.chave == k:
            noAnterior.proximo = noAtual.proximo
            return k

        else:
            noAnterior = noAtual
            noAtual = noAtual.proximo

    return -1
