class No(object):
 
    def __init__(self, chave, anterior, proximo):
        self.chave = chave
        self.anterior = anterior
        self.proximo = proximo
 
class ListaDuplamenteEncadeada:

    cabeca = None
    rabo = None
    def bubblesort(self):
        listaOrdenada = self.cabeca
        
        # cabeça [4 | 1 | 2]
        # [4 | 1 | 2]  -> [1 | 2 | 3]  -> [2 | 3 | 4]
        if listaOrdenada:
            while True:
                if listaOrdenada.proximo != self.cabeca:
                    if(self.cabeca.proximo.chave < listaOrdenada.chave):
                        aux_anterior = listaOrdenada.anterior
                        aux_proximo = listaOrdenada.proximo
                        aux_chave = listaOrdenada.chave

                        self.cabeca.proximo.aux_anterior = listaOrdenada.anterior
                        self.cabeca.proximo.aux_proximo = listaOrdenada.proximo
                        self.cabeca.proximo.chave = listaOrdenada.chave
               
                if listaOrdenada.proximo == self.cabeca:
                    listaOrdenada = None
                else:
                    listaOrdenada = listaOrdenada.proximo

    def buscar(self, chave):
        lista = self.cabeca
        if lista is not None:
            while lista and lista.chave != chave:
                lista = lista.proximo
        else:
            print('Lista vazia.')
        return lista

    def buscarChaveRepetida(self, chave):
        lista = self.cabeca
        if lista is not None:
            while lista and lista.chave != chave:
                lista = lista.proximo
                if lista is None:
                    return False
                if lista.proximo == self.cabeca and lista.chave != chave:
                    return False
            else:
                return True
        else:
            return False        

    def visualizar(self, forma):
        if forma == 1:
            lista = self.cabeca
            if lista:
                while True:
                    print('Chave: {}, chave anterior: {}, chave posterior: {} endereço: {}'.format(lista.chave, lista.anterior.chave if lista.anterior is not None else lista.anterior, lista.proximo.chave if lista.proximo is not None else lista.proximo, hex(id(lista))))
                    if lista.proximo is not None:
                        lista = lista.proximo
                        if lista.chave == self.cabeca.chave:
                            break
                    else:
                        break
            else:
                print('Lista vazia.')
            return lista
        elif forma == 2:
            print('Forma reversa')

            lista = self.rabo
            if lista:
                while True:
                    print('Chave: {}, chave anterior: {}, chave posterior: {} endereço: {}'.format(lista.chave, lista.anterior.chave if lista.anterior is not None else lista.anterior, lista.proximo.chave if lista.proximo is not None else lista.proximo, hex(id(lista))))
                    if lista.anterior is not None:
                        lista = lista.anterior
                        if lista.chave == self.cabeca.chave:                    
                            print('Chave: {}, chave anterior: {}, chave posterior: {} endereço: {}'.format(lista.chave, lista.anterior.chave if lista.anterior is not None else lista.anterior, lista.proximo.chave if lista.proximo is not None else lista.proximo, hex(id(lista))))
                            break
                    else:
                        break
            else:
                print('Lista vazia.')
            return lista
        else:
            print('Ordem de impressão inválida.')

    def inserir(self, chave):
        if self.buscarChaveRepetida(chave) == False:
            novo_no = No(chave, None, None)
            novo_no.anterior = novo_no
            novo_no.proximo = novo_no
            if self.cabeca is None:
                self.chave = chave
                self.cabeca = novo_no
                self.rabo = novo_no

            else:
                novo_no.anterior = self.rabo
                novo_no.proximo = self.cabeca
                self.rabo.proximo = novo_no
                self.cabeca.anterior = novo_no
                self.rabo = novo_no
        else:
            print('Chave já existe.')
 
    def remover(self, chave):
        if self.buscarChaveRepetida(chave) == True:
            no_atual = self.cabeca
    
            while no_atual is not None:
                if no_atual.chave == chave:
                    if no_atual.anterior is None:
                        self.cabeca = no_atual.proximo
                        no_atual.proximo.anterior = None
                    else:
                        no_atual.anterior.proximo = no_atual.proximo
                        no_atual.proximo.anterior = no_atual.anterior
                        print('Removido.')

                if no_atual.proximo == self.cabeca:
                    no_atual = None
                else:
                    no_atual = no_atual.proximo
        else:
            print('Chave não existe.')
 
print('''1 - Inserir
2 - Visualizar
3 - Buscar
4 - Remover
0 - Sair''')
menu = -1
cont = 0
chave = -1
lista = ListaDuplamenteEncadeada()

while menu != 0:
    menu = int(input('Opção menu: '))

    if menu == 1:
        print('\n ------- Inserir -------')
        chave = int(input('Informe a chave: '))
        lista.inserir(chave)
    elif menu == 2: 
        print('\n ------- Visualizar -------')
        menuVisualizar = int(input('1 - Ordem direta \n2 - Ordem reversa \nMenu visualizar:'))
        if menuVisualizar == 1:
            lista.visualizar(1)
        elif menuVisualizar == 2:
            lista.visualizar(2)
            pass
        else:
            print('Valor incorreto.')

    elif menu == 3: 
        print('\n ------- Buscar -------')
        chave = int(input('Informe a chave: '))
        retorno = lista.buscar(chave)
        print('Chave: {}, chave anterior: {}, chave posterior: {} endereço: {}'.format(retorno.chave, retorno.anterior.chave if retorno.anterior is not None else retorno.anterior, retorno.proximo.chave if retorno.proximo is not None else retorno.proximo, hex(id(retorno))))

    elif menu == 4: 
        print('\n ------- Remover -------')
        chave = int(input('Informe a chave que deseja remover: '))
        lista.remover(chave)

    elif menu == 0: 
        pass
    else:
        print('Entrada inválida.') 
else:
    print('Programa encerrado.')