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

def buscarIndice (chave, lista):

    indice = 0
    ultimoLista = lista.ultimo
    dadosLista = lista.dados
    
    i = 0
    while i < ultimoLista and dadosLista[i].chave < chave:
        i = i + 1
    if dadosLista[i].chave == chave:
        indice = i

    return indice

def buscar (chave, lista):
    indice = buscarIndice(chave, lista)
    if indice > 0:
        return lista.dados[indice]
    else:
        return 'NIL'

def inserir (chave, lista):
    ultimoLista = lista.ultimo
    if ultimoLista < lista.maximo:
        if buscarIndice(lista.dados[chave].chave, lista) == 0:
            ultimoLista += 1
            #lista.dados[ultimoLista].chave = chave
            lista.dados[ultimoLista].nome = nome
            lista.dados[ultimoLista].idade = idade
            
            lista.ultimo = ultimoLista
        else:
            print('Nó {} já existe.'.format(chave))
            cont -= 1
    else:
        print('Lista cheia.')
#resolver o indice que está excluindo errado
def remover (chave, lista):
    removido = 'NIL'
    ultimoLista = lista.ultimo
    indice = buscarIndice(chave, lista)
    dadosLista = lista.dados

    if indice != -1:
        #removido = dadosLista[indice]
        for indice in range(ultimoLista + 1):
            dadosLista[indice] = dadosLista[indice + 1]
            dadosLista[indice].chave = indice

        dadosLista[ultimoLista].chave = ultimoLista
        dadosLista[ultimoLista].nome = 'NIL'
        dadosLista[ultimoLista].idade = ''
        lista.ultimo -= 1 
    else:
        print('Nó {} não existe.'.format(chave))
    return removido

numMaxObjetos = int(input("Informe o tamanho máximo de cadastros: "))

print('''1 - Inserir
2 - Visualizar todos
3 - Buscar específico
4 - Remover específico
0 - Sair''')
menu = -1
cont = 0

listaNo = []
for i in  range(1, numMaxObjetos + 1):
    listaNo.append(NoListaSeq(i, 'NIL', ''))

listaSeq = ListaSeq(numMaxObjetos, 0, listaNo)

while menu != 0:
    menu = int(input('Opção: '))

    if menu == 1:
        if cont < numMaxObjetos:
            print('\n ------- Inserir -------')
            nome = input('Informe o nome da pessoa: ')
            idade = input('Informe a idade da pessoa: ')
            inserir(listaNo[cont].chave, listaSeq)
            cont += 1
        else:
            print('Sem espaço para cadastrar novas pessoas.')
    elif menu == 2: 
        print('\n ------- Visualizar -------')
        for i in range(len(listaSeq.dados)):
            if listaSeq.dados[i].nome != 'NIL':
                print('Chave: {} \nNome: {} \nIdade: {}'.format(listaSeq.dados[i].chave, listaSeq.dados[i].nome, listaSeq.dados[i].idade))
                print('--------------')
        
        if cont == 0: 
            print('Nenhum dado encontrado.')
        #cont = 0
    elif menu == 3: 
        print('\n ------- Buscar -------')

    elif menu == 4: 
        print('\n ------- Remover -------')
        chave = int(input('Informe a chave que deseja remover: '))
        remover(chave, listaSeq)

    elif menu == 0: 
        pass
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')