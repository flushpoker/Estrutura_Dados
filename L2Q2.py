class NoListaSeq:

    def __init__(self, chave, nome, idade):
        self.chave = chave
        self.nome = nome
        self.idade = idade

class ListaSeq:

    def __init__ (self, maximo, ultimo, dados):
        self.maximo = maximo
        self.ultimo = ultimo
        self.dados = dados

def duplicarTamanhoMaxNo (tamanhoVetor, lista):
    noListaSeq = lista.dados
    for i in range(tamanhoVetor - 1, tamanhoVetor * 2):
        noListaSeq.append(NoListaSeq(i + 1, 'NIL', ''))
        lista.maximo += 1
    
    return noListaSeq
    

def buscarIndice (chave, lista):

    indice = -1
    dadosLista = lista.dados
    
    i = 0
    while i < chave and dadosLista[i].chave < chave:
        i = i + 1
    if dadosLista[i].chave == chave:
        return i

    return indice

def buscar (chave, lista):
    indice = buscarIndice(chave, lista)
    if indice > -1:
        print('Chave: {} \nNome: {} \nIdade: {}'.format(listaSeq.dados[indice].chave, listaSeq.dados[indice].nome, listaSeq.dados[indice].idade))
    #else:
    #    print('NIL')

def inserir (chave, lista):
    if lista.ultimo < lista.maximo - 1:
        retBuscaIndice = buscarIndice(chave, lista)
        if retBuscaIndice != -1:
            #lista.dados[retBuscaIndice].chave = chave
            lista.dados[retBuscaIndice].nome = nome
            lista.dados[retBuscaIndice].idade = idade
            lista.ultimo += 1
            print('Cadastro realizado.')

        else:
            print('Nó {} já existe.'.format(chave))
    else:
        opDuplicarVetor = int(input('Limite de cadastro atingido. Deseja aumentar esse limite (0 - não | 1 - sim)? '))
        if opDuplicarVetor == 1:
            lista.dados = duplicarTamanhoMaxNo(lista.maximo + 1, lista)
            inserir(listaSeq.ultimo + 1, lista)

def remover (chave, lista):
    ultimoLista = lista.ultimo
    indice = buscarIndice(chave, lista)
    dadosLista = lista.dados

    if indice != -1 and dadosLista[indice].nome != 'NIL':
        for i in range(indice, ultimoLista + 1):
            #dadosLista[i].chave = dadosLista[i + 1].chave
            dadosLista[i].nome = dadosLista[i + 1].nome
            dadosLista[i].idade = dadosLista[i + 1].idade

        dadosLista[ultimoLista].chave = ultimoLista
        dadosLista[ultimoLista].nome = 'NIL'
        dadosLista[ultimoLista].idade = ''
        lista.ultimo -= 1 
        print('Removido com sucesso.')
    else:
        print('Não foi possível remover esta chave.')

tamanhoVetor = int(input("Informe o tamanho máximo inicial de cadastros: "))

print('''1 - Inserir
2 - Visualizar todos
3 - Buscar específico
4 - Remover específico
0 - Sair''')
menu = -1

listaNo = []
for i in  range(0, tamanhoVetor + 1):
    listaNo.append(NoListaSeq(i, 'NIL', ''))

listaSeq = ListaSeq(tamanhoVetor, -1, listaNo)

while menu != 0:
    menu = int(input('Opção: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        nome = input('Informe o nome da pessoa: ')
        idade = input('Informe a idade da pessoa: ')
        inserir(listaNo[listaSeq.ultimo + 1].chave, listaSeq)

    elif menu == 2: 
        print('\n ------- Visualizar -------')
        for i in range(listaSeq.ultimo + 1):
            if listaSeq.dados[i].nome != 'NIL':
                print('Chave: {} \nNome: {} \nIdade: {}'.format(listaSeq.dados[i].chave, listaSeq.dados[i].nome, listaSeq.dados[i].idade))
                print('--------------')
        
    elif menu == 3: 
        print('\n ------- Buscar -------')
        chave = int(input('Informe a chave da pessoa que deseja buscar os dados: '))
        buscar(chave, listaSeq)

    elif menu == 4: 
        print('\n ------- Remover -------')
        chave = int(input('Informe a chave da pessoa que deseja remover: '))
        remover(chave, listaSeq)
        
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')