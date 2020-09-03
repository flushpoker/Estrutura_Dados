# Implemente, em uma Linguagem de Programação, o algoritmo Heapsort, que recebe um
# vetor de dados de tamanho M, completamente preenchido pelo usuário, como entrada.
# Implemente as Estruturas de Dados básicas necessárias. Imprima o vetor de dados original
# (passado como entrada ao algoritmo). Imprima o vetor de dados gerado após a execução do
# procedimento construirMaxHeap. Ao final de cada execução do procedimento
# particionar, o vetor de dados modificado deve ser impresso. Imprima o número total
# de vezes que o procedimento trocar é utilizado durante a execução do algoritmo. Imprima
# o número total de vezes que o procedimento maxHeapfy é utilizado durante a execução do
# algoritmo. (4.0 pontos)

contTroca = 0
def trocar(A, i, j):
    global contTroca
    aux = A[j]
    A[j] = A[i]
    A[i] = aux

    #A[i], A[j] = A[j], A[i]
    contTroca += 1

def heapsort(A, tamanhoHeap):
    tamanhoA = tamanhoHeap
    construirMaxHeap(A, tamanhoA)
    for i in range(tamanhoHeap - 1, 0, -1):
        trocar(A, i, 0)
        maxHeapfy(A, 0, i)
        print('Lista particionar: {}'.format(A))
    return A
    

def construirMaxHeap(A, tamanhoHeap):
    for i in range(int(tamanhoHeap / 2) - 1, -1, -1):
        maxHeapfy(A, i, tamanhoHeap)
    print('Lista construir max heap: {}'.format(A))
        

def maxHeapfy(A, i, tamanhoHeap):
    l = retornaIndiceFilhoEsquerda(i)
    r = retornaIndiceFilhoDireita(i)

    if (l < tamanhoHeap) and (A[i] < A[1]):
        maior = l
    else:
        maior = i
    if (r < tamanhoHeap) and (A[maior] < A[r]):
        maior = r
    if maior != i:
        trocar(A, i, maior)
        maxHeapfy(A, maior, tamanhoHeap)

def retornaIndiceFilhoEsquerda(i):
    return i * 2 + 1

def retornaIndiceFilhoDireita(i):
    return 2 * (i + 1)

def criaVetorEstatico(fim):
    vetor = []
    for _ in range(0, fim):
        vetor.append(None)
    return vetor

lenArray = int(input('Informe o tamanho do array: '))
lista = criaVetorEstatico(lenArray)
for i in range(0, lenArray):
    lista[i] = int(input('{}° valor: '.format(i + 1)))
print('Lista inicial: {}'.format(lista))
heapsort(lista, lenArray)

print('Lista ordenada: {}'.format(lista))
print('Quantidade total de trocas: {}'.format(contTroca))