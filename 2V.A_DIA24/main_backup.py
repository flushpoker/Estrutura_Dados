from math import ceil

class Dados:
    def __init__(self, linha_1, linha_2):
        self.linha_1 = linha_1
        self.linha_2 = linha_2

class NoHashTableClosed:
    def __init__(self, chave, proximo, capacidade_coleta, distBase):
        self.chave = chave
        self.cabeca = None
        self.proximo = proximo
        self.capacidade_coleta = capacidade_coleta
        self.distBase = distBase
        self.distBaseAtual = self.distBase
        self.vaiBase = True
        self.inventario = 0

class NoHashTableOpen:
    def __init__(self, chave, capacidade_coleta, distBase):
        self.chave = chave
        self.cabeca = None
        self.proximo = None
        self.capacidade_coleta = capacidade_coleta
        self.distBase = distBase
        self.distBaseAtual = self.distBase
        self.vaiBase = True
        self.inventario = 0

class Base:
    def __init__(self):
        self.minerios = 0
        self.mineradores = []

class Mina:
    def __init__(self, tamanho, qtdAtual):
        self.tamanho = tamanho
        self.mineradores = [] #
        for _ in range(0, tamanho):
            self.mineradores.append(None)
        self.qtdAtual = qtdAtual


    def hashFunction(self, chave, tamanho):
        return chave % tamanho

    def inserirTabelaHashClosed(self, chave, capacidade_coleta, distBase, tamanho):            
        self.inserir(chave, capacidade_coleta, distBase, tamanho)
        #self.qtdAtual += 1

    def inserirTabelaHashOpen(self, chave, capacidade_coleta, distBase, tamanho):
        funcao_hash = self.hashFunction(chave, tamanho)
        novo_no = NoHashTableOpen(chave, capacidade_coleta, distBase)
        indice = 0
        if self.mineradores[funcao_hash] is None:
            self.mineradores[funcao_hash] = novo_no
            indice = funcao_hash
            print('minerador {} inserido na mina {}.'.format(chave, funcao_hash))
        else:
            i = (funcao_hash % self.tamanho) + 1
            while i != funcao_hash:
                if self.mineradores[i] is None:
                    self.mineradores[i] = novo_no
                    print('minerador {} colidiu com minerador {} na mina {}.'.format(chave, self.mineradores[funcao_hash].chave, funcao_hash))
                    print('minerador {} inserido na mina {}.'.format(chave, i))
                    indice = i
                    i = funcao_hash
                    
                else:
                    i = (i % self.tamanho) + 1
            if indice == 0:
                print('Overflow')

        
        self.qtdAtual += 1
        return indice

    def inserir(self, chave, capacidade_coleta, distBase, tamanho):
        self.cabeca = None
        funcao_hash = self.hashFunction(chave, tamanho)
        if self.cabeca:
            novo_no = self.cabeca
            while(novo_no.proximo):
                novo_no = novo_no.proximo
            novo_no.proximo = NoHashTableClosed(chave, None, capacidade_coleta, distBase)
        else:
            self.cabeca = NoHashTableClosed(mina.mineradores[funcao_hash].chave, None, mina.mineradores[funcao_hash].capacidade_coleta, mina.mineradores[funcao_hash].distBase)
            self.cabeca.proximo = NoHashTableClosed(chave, None, capacidade_coleta, distBase)
            mina.mineradores[funcao_hash].cabeca = self.cabeca
        
        print('minerador {} inserido na fila de espera da mina {}.'.format(chave, funcao_hash))

    def inserir_minerador(self, chave, capacidade_coleta, distBase, tamanho):
        if mina.qtdAtual >= mina.tamanho:
            mina.inserirTabelaHashClosed(chave, capacidade_coleta, distBase, tamanho)
        else:
            mina.inserirTabelaHashOpen(chave, capacidade_coleta, distBase, tamanho)

    def imprimir_mineradores(self):
        for i in range(mina.tamanho):
            if mina.mineradores[i]:
                print('{}({}) '.format(mina.mineradores[i].chave, mina.mineradores[i].inventario), end='')
            else:
                print('vazia ',end='')
        print('')

menu = int(input('\n1 - Inserir dados por aquivo \n2 - Inserir dados manualmente \n0 - Sair: '))
dados_iniciais = []
tListaMina = -3 #modelo para pegar o tamanho da mina (a cada 3 linhas pega o primeiro elemento da linha)
tListaMinarador = -3
if menu == 1:
    print('\n ------- Inserir Por Arquivo -------')
    caminho = input('Informe o caminho do arquivo .txt: ')
    dados_iniciais = open(caminho, "r").readlines()

elif menu == 2: 
    print('\n ------- Inserir Manualmente -------')
    print('Informe duas linhas, com as seguintes informações')
    print('Linha 1: t n d r \nonde t é o tamanho da mina, n é o número de mineradores, d é a distância à base e r é o número de turnos que o jogo terá. ')
    print('Linha 2: a linha 2 conterá 2n valores, correspondendo cada dupla de valores a um dos n mineradores, sendo o primeiro valor sua chave e o segundo sua capacidade de coleta máxima. ')
    
    dados_linha1 = ''
    while (dados_linha1 != '0'):
        dados_linha1 = input('Informe a primeira linha (0 para iniciar jogo): ')
        if dados_linha1 != '0':
            dados_linha2 = input('Informe a segunda linha: ')
            dados_iniciais.append(dados_linha1)
            dados_iniciais.append(dados_linha2)
            dados_iniciais.append('\n')

for r in range(0, len(dados_iniciais), 3):
    print('novo jogo comecou.')
    mina = Mina(int(dados_iniciais[r].split(' ')[0]), 0) #pega o primeiro elemento da string
    base = Base()

    print('etapa de inicializacao.')
    i_minerador = 0
    for _ in range(0, int(dados_iniciais[tListaMina + 3].split(' ')[1])):
        mina.inserir_minerador(int(dados_iniciais[tListaMinarador + 4].split(' ')[i_minerador]), int(dados_iniciais[tListaMinarador + 4].split(' ')[i_minerador + 1]), int(dados_iniciais[tListaMina + 3].split(' ')[2]), mina.tamanho)
        i_minerador += 2


    for ii in range(0, int(dados_iniciais[tListaMina + 3].split(' ')[3]) + 1):
        mina.imprimir_mineradores()

        for i in range(0, mina.tamanho):
            if mina.mineradores[i]: 
                if mina.mineradores[i].inventario < mina.mineradores[i].capacidade_coleta:
                    mina.mineradores[i].inventario += 1
                else:
                    print('minerador {} a caminho da base.'.format(mina.mineradores[i].chave))

                    base.mineradores.append(mina.mineradores[i]) #criar um append
                    if mina.mineradores[i].cabeca:
                        if mina.mineradores[i].cabeca.proximo:
                            mina.mineradores[i] = mina.mineradores[i].cabeca.proximo
                    else:
                        mina.mineradores[i] = None
                    mina.qtdAtual -= 1

                        

        if base.mineradores:
            for i in range(0, len(base.mineradores)):
                if base.mineradores[i]:
                    if base.mineradores[i].vaiBase:
                        if base.mineradores[i].distBaseAtual > 0:
                            base.mineradores[i].distBaseAtual -= 1
                        else:
                            base.minerios += base.mineradores[i].inventario
                            print('minerador {} depositou {} minerio(s) na base.'.format(base.mineradores[i].chave, base.mineradores[i].inventario))
                            base.mineradores[i].vaiBase = False
                            base.mineradores[i].distBaseAtual = base.mineradores[i].distBase

                    if base.mineradores[i].vaiBase is not True:
                        if base.mineradores[i].distBaseAtual > 0:
                            base.mineradores[i].distBaseAtual -= 1
                        else:
                            base.mineradores[i].vaiBase = True
                            base.mineradores[i].distBaseAtual = base.mineradores[i].distBase
                            
                            print('minerador {} retornou as minas.'.format(base.mineradores[i].chave))
                            mina.inserir_minerador(base.mineradores[i].chave, base.mineradores[i].capacidade_coleta, base.mineradores[i].distBase, mina.tamanho)
                            base.mineradores[i] = None
        if ii != 0:
            print('base: {}.'.format(base.minerios))
        if ii != int(dados_iniciais[tListaMina + 3].split(' ')[3]):
            print('turno {} comecou.'.format(ii + 1)) 


    print('fim de jogo. {} minerios coletados.'.format(base.minerios))
    print('\n\n')