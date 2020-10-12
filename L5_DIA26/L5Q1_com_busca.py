class NoHashTable:
    def __init__(self, chave, proximo, dado):
        self.chave = chave
        self.proximo = proximo
        self.dado = dado

class TabelaHashClosed:
    def __init__ (self, tamanho, cabeca, tabela):
        self.tamanho = tamanho
        self.cabeca = cabeca
        self.tabela = [] #listaLinearEncadeada

class HashTable:
    def __init__(self, tamanho, qtdAtual):
        self.tamanho = tamanho
        self.tabela = []
        for _ in range(0, tamanho):
            self.tabela.append(None)
        self.qtdAtual = qtdAtual

    cabeca = None

    def hashFunction(self, chave, tamanho):
        return chave % tamanho

    def buscarTabelaHashClosed(self, chave, tabela): #listaLinearEncadeada
        funcao_hash = self.hashFunction(chave, tabela.tamanho)
        return self.buscar(chave)

    def inserirTabelaHashClosed(self, chave, dado):
        funcao_hash = self.hashFunction(chave, self.tamanho)
        self.inserir(funcao_hash, dado)
        self.qtdAtual += 1

    def buscarTabelaHashOpen(self, chave, tabela): #listaLinearEncadeada
        funcao_hash = self.hashFunction(chave, tabela.tamanho)
        endereco = None
        if tabela.tamanho is not None and tabela.tabela[funcao_hash].chave == chave:
            endereco = tabela.tabela[funcao_hash]
        else:
            i = (funcao_hash % tabela.tamanho) + 1
            while i != funcao_hash:
                if tabela.tabela[i] and tabela.tabela[i].chave == chave:
                    endereco = tabela.tabela[i]
                    i = funcao_hash
                else:
                    i = (i % tabela.tamanho) + 1

        return endereco

    def inserirTabelaHashOpen(self, chave, dado):
        funcao_hash = self.hashFunction(chave, tamanho)
        indice = 0
        if self.tabela[funcao_hash] is None:
            self.tabela[funcao_hash] = chave
            indice = funcao_hash
        else:
            i = (funcao_hash % self.tamanho) + 1
            while i != funcao_hash:
                if self.tabela[i] is None:
                    self.tabela[i] = chave
                    indice = i
                    i = funcao_hash
                else:
                    i = (i % self.tamanho) + 1
            if indice == 0:
                print('Overflow')
        
        self.qtdAtual += 1
        return indice

    def buscar(self, chave):
        tabela = self.cabeca
        if tabela is not None:
            while tabela and tabela.chave != chave:
                tabela = tabela.proximo
        else:
            print('tabela vazia.')
        return tabela

    def inserir(self, chave, dado):
        #self, chave, proximo, dado
        novo_no = NoHashTable(chave, None, dado)
        novo_no.proximo = novo_no
        if self.cabeca is None:
            self.chave = chave
            self.dado = dado

        else:
            novo_no.proximo = self.cabeca
            #self.cabeca.anterior = novo_no

tamanho = int(input('Informe o tamanho máximo da tabela: '))
print('''1 - Inserir
2 - Buscar
0 - Sair''')
menu = -1
lista = HashTable(tamanho, 0)

while menu != 0:
    menu = int(input('Opção menu: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        chave = int(input('Informe a chave: '))
        dado = input('Informe o que deseja inserir: ')

        if lista.qtdAtual == lista.tamanho:
            lista.inserirTabelaHashClosed(chave, dado)
        else:
            lista.inserirTabelaHashOpen(chave, dado)

    elif menu == 2: 
        print('\n ------- Visualizar -------')
        chave = int(input('Informe a chave: '))
        lista.buscar(chave)
    elif menu == 0: 
        pass
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')