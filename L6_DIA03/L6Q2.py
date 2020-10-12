class NoArvoreBi:
    def __init__(self, chave, dado, pai=None, esquerda=None, direita=None):
        self.chave = chave
        self.dado = dado
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

def encontrarMaximo(no_arvore):
    while no_arvore.direita != None:
        no_arvore = no_arvore.direita
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

def buscarArvoreBinRec(chave, no_raiz):
    if no_raiz == None or no_raiz.chave == chave:
        return no_raiz
    elif chave < no_raiz.chave:
        return buscarArvoreBinRec(chave, no_raiz.esquerda)
    else:
        return  buscarArvoreBinRec(chave, no_raiz.direita)

def consultarChaveDisponivel(chave, no_raiz):
    while no_raiz != None:
        if chave < no_raiz.chave:
            if chave == no_raiz.chave:
                return False
            no_raiz = no_raiz.esquerda
        else:
            if chave == no_raiz.chave:
                return False
            no_raiz = no_raiz.direita

    return True

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

def removerArvoreBin(chave, raiz):
    no_arvore = buscarArvoreBinRec(chave, raiz.raiz)

    if no_arvore == None:
        print('Nó {} inexistente.'.format(chave))
    else:
        if no_arvore.esquerda == None and no_arvore.direita == None:
            removerSemFilhos(no_arvore, raiz)
        elif no_arvore.esquerda != None and no_arvore.direita != None:
            removerDoisFilhos(no_arvore, raiz)
        else:
            removerUnicoFilho(no_arvore, raiz)
    return no_arvore

def removerSemFilhos(no_arvore, raiz):
    pai = no_arvore.pai
    if pai != None:
        if pai.chave >= no_arvore.chave:
            pai.esquerda = None
        else:
            pai.direita = None
    else:
        raiz.raiz = None
    no_arvore.pai = None

def removerUnicoFilho(no_arvore, raiz):
    pai = no_arvore.pai
    filho = None
    if no_arvore.esquerda != None:
        filho = no_arvore.esquerda
        no_arvore.esquerda = None
    else:
        filho = no_arvore.direita
        no_arvore.direita = None

    if pai != None:
        filho.pai = pai
        if filho.chave <= pai.chave:
            pai.esquerda = filho
        else:
            pai.direita = filho
    else:
        raiz.raiz = filho
    raiz.pai = None

def removerDoisFilhos(no_arvore, raiz):
    sucessor = encontrarSucessor(no_arvore)
    sucessor = removerArvoreBin(sucessor.chave, raiz)

    sucessor.pai = no_arvore.pai
    no_arvore.pai = None
    sucessor.esquerda = no_arvore.esquerda
    no_arvore.esquerda = None
    sucessor.direita = no_arvore.direita
    no_arvore.direita = None
    pai = sucessor.pai

    if pai != None:
        if pai.chave >= sucessor.chave:
            pai.esquerda = sucessor
        else:
            pai.direita = sucessor
    else:
        raiz.raiz = sucessor

    sucessor.esquerda.pai = sucessor
    if  sucessor.direita != None:
        sucessor.direita.pai = sucessor

menu = -1
raiz = ArvoreBin(None)

while menu != 0:
    print('\n1 - Inserir \n2 - Buscar \n3 - Remover \n0 - Sair')
    menu = int(input('Opção menu: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        chave = int(input('Informe a chave: '))
        dado = input('Informe o que deseja inserir: ')
        no_arvore = NoArvoreBi(chave, dado)
        if consultarChaveDisponivel(chave, raiz.raiz):
            inserirArvoreBin(no_arvore, raiz)
        else:
            print('Chave indisponível.')
        
    elif menu == 2: 
        print('\n ------- Buscar -------')
        chave = int(input('Informe a chave: '))
        no_arvore = buscarArvoreBinRec(chave, raiz.raiz)
        print('O dado da chave {} é: {}'.format(chave, no_arvore.dado if no_arvore != None else no_arvore))

    elif menu == 3: 
        print('\n ------- Remover -------')
        chave = int(input('Informe a chave que deseja remover: '))
        removerArvoreBin(chave, raiz)
            
    elif menu == 0: 
        pass
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')