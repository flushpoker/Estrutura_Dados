class NoArvoreBi:
    def __init__(self, chave, pai=None, esquerda=None, direita=None):
        self.chave = chave
        self.pai = pai #NoArvoreBi
        self.esquerda = esquerda #NoArvoreBi
        self.direita = direita #NoArvoreBi

class ArvoreBin:
    def __init__(self, raiz=None):
        self.raiz = raiz #NoArvoreBi

def encontrarMinimo(no_arvore):
    while no_arvore.esquerda != None:
        no_arvore = no_arvore.esquerda
    return no_arvore

def encontrarSucessor(no_arvore):
    if no_arvore.direita != None:
        return encontrarMinimo(no_arvore.direita)
    else:
        pai = no_arvore.pai
        while pai != None and no_arvore.chave == pai.direita.chave:
            no_arvore = pai
            pai = pai.pai
        return pai

def buscarArvoreBinRec(chave, no_arvore):
    if no_arvore == None or no_arvore.chave == chave:
        return encontrarSucessor(no_arvore)
    elif chave < no_arvore.chave:
        return buscarArvoreBinRec(chave, no_arvore.esquerda)
    else:
        return  buscarArvoreBinRec(chave, no_arvore.direita)

def inserirArvoreBin(no_arvore, raiz):
    pai = None
    raiz_arvore = raiz.raiz
    while raiz_arvore != None:
        pai = raiz_arvore
        if no_arvore.chave <= raiz_arvore.chave:
            raiz_arvore = raiz_arvore.esquerda
        else:
            raiz_arvore = raiz_arvore.direita

    no_arvore.pai = pai
    if pai == None:
        raiz.raiz = no_arvore
    elif no_arvore.chave <= pai.chave:
        pai.esquerda = no_arvore
    else:
        pai.direita = no_arvore

#valores = [45, 18, 30, 60, 81, 96, 101, 5, 8, 3]
valores = [15, 6, 3, 2, 4, 7, 13, 9, 18, 16, 20]
raiz = ArvoreBin(NoArvoreBi(valores[0]))
for i in range(1, len(valores)):
    no_arvore = NoArvoreBi(valores[i])
    inserirArvoreBin(no_arvore, raiz)

print('Chaves disponíveis: {}'.format(valores))
chave = int(input('Informe uma chave: '))
sucessor = buscarArvoreBinRec(chave, raiz.raiz)
print('O sucessor de {} é: {}'.format(chave, sucessor.chave if sucessor != None else sucessor))