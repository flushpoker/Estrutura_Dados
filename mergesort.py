def criaVetorEstatico(tamanho):
    vetor = []
    for _ in range(0, tamanho):
        vetor.append(None)
    return vetor

def mergesort(lista, inicio, fim):
    if fim - inicio > 1:
        if (inicio + fim) % 2 == 0:
            meio = int((inicio + fim) / 2)
        else:
            meio = int((inicio + fim - 1) / 2)

        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
        print('Merge atual:   {}'.format(lista))

def merge(lista, inicio, meio, fim):
    lista_esquerda = criaVetorEstatico(meio - inicio)
    lista_direita = criaVetorEstatico(fim - meio)
    
    j, k = 0, 0
    for i in range(0, meio - inicio):
        lista_esquerda[i] = lista[inicio + i]
        j += 1

    for i in range(0, fim - meio):
        lista_direita[i] = lista[i + meio]
        k += 1

    topo_direita, topo_esquerda = 0, 0
    for i in range(inicio, fim):
        if topo_esquerda >= len(lista_esquerda):
            lista[i] = lista_direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(lista_direita):
            lista[i] = lista_esquerda[topo_esquerda]
            topo_esquerda += 1
        elif lista_direita[topo_direita] < lista_esquerda[topo_esquerda]:
            lista[i] = lista_direita[topo_direita]
            topo_direita += 1
        else:
            lista[i] = lista_esquerda[topo_esquerda]
            topo_esquerda += 1

lenArray = int(input('Informe o tamanho do array: '))
lista = criaVetorEstatico(lenArray)
    
for i in range(0, lenArray):
    lista[i] = int(input('{}° valor: '.format(i + 1)))
print('Lista inicial: {}'.format(lista))
mergesort(lista, 0, lenArray)