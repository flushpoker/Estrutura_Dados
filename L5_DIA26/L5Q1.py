class NoHashTableClosed:
    def __init__(self, chave, proximo, dado):
        self.chave = chave
        self.proximo = proximo
        self.dado = dado

class NoHashTableOpen:
    def __init__(self, chave, dado):
        self.chave = chave
        self.dado = dado

class HashTable:
    def __init__(self, tamanho, qtdAtual):
        self.tamanho = tamanho
        self.tabela = [] #
        for _ in range(0, tamanho):
            self.tabela.append(None)
        self.qtdAtual = qtdAtual

    cabeca = None

    def hashFunction(self, chave, tamanho):
        return chave % tamanho

    def inserirTabelaHashClosed(self, chave, dado):            
        self.inserir(chave, dado)
        self.qtdAtual += 1

    def inserirTabelaHashOpen(self, chave, dado):
        funcao_hash = self.hashFunction(chave, tamanho)
        novo_no = NoHashTableOpen(chave, dado)
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
        return indice

    def inserir(self, chave, dado):
        funcao_hash = self.hashFunction(chave, tamanho)
        if self.cabeca:
            novo_no = self.cabeca
            while(novo_no.proximo):
                novo_no = novo_no.proximo
            novo_no.proximo = NoHashTableClosed(chave, None, dado)
        else:
            self.cabeca = NoHashTableClosed(lista.tabela[funcao_hash].chave, None, lista.tabela[funcao_hash].dado)
            self.cabeca.proximo = NoHashTableClosed(chave, None, dado)
            lista.tabela[funcao_hash] = self.cabeca

tamanho = int(input('Informe o tamanho máximo da tabela: '))
print('''1 - Inserir
0 - Sair''')
menu = -1
lista = HashTable(tamanho, 0)

while menu != 0:
    menu = int(input('Opção menu: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        chave = int(input('Informe a chave: '))
        dado = input('Informe o que deseja inserir: ')

        if lista.qtdAtual >= lista.tamanho:
            lista.inserirTabelaHashClosed(chave, dado)
        else:
            lista.inserirTabelaHashOpen(chave, dado)
    elif menu == 0: 
        pass
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')