def criaVetorEstatico(tamanho):
    vetor = []
    for _ in range(0, tamanho):
        vetor.append(None)
    return vetor

def quicksort(lista, inicio, fim):
    if inicio < fim:
        p = particionar(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)

def particionar(lista, inicio, fim):
    fim -= 1
    pivor = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivor:
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
            i += 1
    aux1 = lista[i]
    lista[i] = lista[fim]
    lista[fim] = aux1
    print('Merge atual:  {}'.format(lista))
    return i


lenArray = int(input('Informe o tamanho do array: '))
lista = criaVetorEstatico(lenArray)
    
for i in range(0, lenArray):
    lista[i] = int(input('{}° valor: '.format(i + 1)))
print('Lista inicial: {}'.format(lista))
quicksort(lista, 0, lenArray)