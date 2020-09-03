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

    indice = -1
    ultimoLista = lista.ultimo
    dadosLista = lista.dados
    
    i = 0
    while i < ultimoLista and dadosLista[i].chave <= chave:
        i = i + 1
    if dadosLista[i].chave == chave:
        return i

    return indice - 1

def buscar (chave, lista):
    indice = buscarIndice(chave, lista)
    if indice > -1:
        return lista.dados[indice]
    else:
        return 'NIL'

def inserir (chave, lista):
    ultimoLista = lista.ultimo
    if ultimoLista < lista.maximo:
        if buscarIndice(lista.dados[chave].chave, lista) == -2:
            #lista.dados[ultimoLista].chave = chave
            lista.dados[ultimoLista].nome = nome
            lista.dados[ultimoLista].idade = idade
            ultimoLista += 1
            
            lista.ultimo = ultimoLista
        else:
            print('Nó {} já existe.'.format(chave))
    else:
        print('Lista cheia.')
#resolver o indice que não cadastra após excluir uma pessoa
def remover (chave, lista):
    ultimoLista = lista.ultimo
    indice = buscarIndice(chave, lista)
    dadosLista = lista.dados
    removido = dadosLista[indice]

    if indice != -1:
        removido = dadosLista[indice]
        for indice in range(ultimoLista):
            #dadosLista[indice].chave = dadosLista[indice + 1].chave
            dadosLista[indice].nome = dadosLista[indice + 1].nome
            dadosLista[indice].idade = dadosLista[indice + 1].idade

        dadosLista[ultimoLista].chave = ultimoLista
        dadosLista[ultimoLista].nome = 'NIL'
        dadosLista[ultimoLista].idade = ''
        lista.ultimo -= 1 
        print('Removido com sucesso.')
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

listaNo = []
for i in  range(1, numMaxObjetos + 2):
    listaNo.append(NoListaSeq(i, 'NIL', ''))

listaSeq = ListaSeq(numMaxObjetos, 0, listaNo)

while menu != 0:
    menu = int(input('Opção: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        nome = input('Informe o nome da pessoa: ')
        idade = input('Informe a idade da pessoa: ')
        inserir(listaNo[listaSeq.ultimo].chave, listaSeq)
    
    #print('Sem espaço para cadastrar novas pessoas.')

    elif menu == 2: 
        print('\n ------- Visualizar -------')
        for i in range(len(listaSeq.dados)):
            if listaSeq.dados[i].nome != 'NIL':
                print('Chave: {} \nNome: {} \nIdade: {}'.format(listaSeq.dados[i].chave, listaSeq.dados[i].nome, listaSeq.dados[i].idade))
                print('--------------')
        
         
        #print('Nenhum dado encontrado.')
        
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