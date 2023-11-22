# Busca, Inserção e Remoção em filas


# --------------- Codigo de Busca ---------------


# --------------- Codigo de Inserção ---------------

# Encadeado:
def insere(self, novoNo):
    if self.inicio == None:
        self.inicio = novoNo
        self.final = novoNo

    else:
        self.final.proximo = novoNo
        self.final = novoNo


# Contigua:
def insereFila(novoNo):
    global inicioFila
    global maxFila
    global finalFila
    global fila

    if inicioFila == None:
        fila[0] = novoNo
        inicioFila = 0
        finalFila = 0
    elif (finalFila + 1) % maxFila == inicioFila:
        # Fila cheia -> Overflow
        return -1
    else:
        finalFila = (finalFila + 1) % maxFila
        fila[finalFila] = novoNo

    return finalFila


# --------------- Codigo de Remoção ---------------

# Encadeado:
def remove(self):
    if self.inicio == None:
        # Erro de fila vazia
        return None
    else:
        k = self.inicio
        self.inicio = self.inicio.proximo
        return k


# Contigua:
def removeFila():
    global inicioFila
    global maxFila
    global finalFila
    global fila

    if inicioFila == None:
        # Fila vazia
        return None

    k = fila[inicioFila]
    if finalFila == inicioFila:
        inicioFila = None
        # Fila vazia após remoção
    else:
        inicioFila = (inicioFila + 1) % maxFila
        # remove o nó

    return k
