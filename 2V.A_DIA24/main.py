class Dados:
    def __init__(self, linha_1, linha_2):
        self.linha_1 = linha_1
        self.linha_2 = linha_2

class NoHashTableClosed:
    def __init__(self, chave, proximo, capacidade_coleta):
        self.chave = chave
        self.proximo = proximo
        self.capacidade_coleta = capacidade_coleta

class NoHashTableOpen:
    def __init__(self, chave, capacidade_coleta):
        self.chave = chave
        self.capacidade_coleta = capacidade_coleta

class Mina:
    def __init__(self, tamanho, qtdAtual):
        self.tamanho = tamanho
        self.tabela = [] #
        for _ in range(0, tamanho):
            self.tabela.append(None)
        self.qtdAtual = qtdAtual

    cabeca = None

    def hashFunction(self, chave, tamanho):
        return chave % tamanho

    def inserirTabelaHashClosed(self, chave, capacidade_coleta, tamanho):            
        self.inserir(chave, capacidade_coleta, tamanho)
        self.qtdAtual += 1

    def inserirTabelaHashOpen(self, chave, capacidade_coleta, tamanho):
        funcao_hash = self.hashFunction(chave, tamanho)
        novo_no = NoHashTableOpen(chave, capacidade_coleta)
        indice = 0
        if self.tabela[funcao_hash] is None:
            self.tabela[funcao_hash] = novo_no
            indice = funcao_hash
        else:
            i = (funcao_hash % self.tamanho) + 1
            while i != funcao_hash:
                if self.tabela[i] is None:
                    self.tabela[i] = novo_no
                    indice = i
                    i = funcao_hash
                else:
                    i = (i % self.tamanho) + 1
            if indice == 0:
                print('Overflow')
        
        self.qtdAtual += 1
        print('minerador {} inserido na mina {}.'.format(chave, funcao_hash))
        return indice

    def inserir(self, chave, capacidade_coleta, tamanho):
        funcao_hash = self.hashFunction(chave, tamanho)
        if self.cabeca:
            novo_no = self.cabeca
            while(novo_no.proximo):
                novo_no = novo_no.proximo
            novo_no.proximo = NoHashTableClosed(chave, None, capacidade_coleta)
        else:
            self.cabeca = NoHashTableClosed(mina.tabela[funcao_hash].chave, None, mina.tabela[funcao_hash].capacidade_coleta)
            self.cabeca.proximo = NoHashTableClosed(chave, None, capacidade_coleta)
            mina.tabela[funcao_hash] = self.cabeca
        
        print('minerador {} inserido na fila de espera da mina {}.'.format(chave, funcao_hash))

    def inserir_minerador(self, chave, capacidade_coleta, tamanho):
        if mina.qtdAtual >= mina.tamanho:
            mina.inserirTabelaHashClosed(chave, capacidade_coleta, tamanho)
        else:
            mina.inserirTabelaHashOpen(chave, capacidade_coleta, tamanho)


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
        dados_linha1 = input('Informe a primeira linha (0 para sair): ')
        if dados_linha1 != '0':
            dados_linha2 = input('Informe a segunda linha: ')
            dados_iniciais.append(dados_linha1)
            dados_iniciais.append(dados_linha2)
            dados_iniciais.append('\n')

print('novo jogo comecou.')
mina = Mina(int(dados_iniciais[tListaMina + 3].split(' ')[0]), 0) #pega o primeiro elemento da string

print('etapa de inicializacao.')

i_minerador = 0
for _ in range(0, int(dados_iniciais[tListaMina + 3].split(' ')[1])):
    mina.inserir_minerador(int(dados_iniciais[tListaMinarador + 4].split(' ')[i_minerador]), int(dados_iniciais[tListaMinarador + 4].split(' ')[i_minerador + 1]), mina.tamanho)
    i_minerador = i_minerador + 2


'''
Linha 1: t n d r
onde t é o tamanho da mina, n é o número de mineradores, d é a distância à base e r é o número de turnos
que o jogo terá.
Linha 2: a linha 2 conterá 2n valores, correspondendo cada dupla de valores a um dos n mineradores, sendo
o primeiro valor sua chave e o segundo sua capacidade de coleta máxima. 


O jogo começa com uma etapa de inicialização (turno 0), onde cada minerador é atribuído à sua posição
inicial. A mina suportará no máximo t mineradores por vez, sendo as posições dos mesmos na mina
resolvidas através da técnica de hashing baseada na chave de cada minerador.
'''
