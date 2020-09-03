def criaVetorEstatico(tamanho):
    vetor = []
    for _ in range(0, tamanho):
        vetor.append(None)
    return vetor

def quicksort(lista, inicio, fim):
    if inicio < fim:
        p = particionar(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p - 1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p + 1, fim)

def particionar(lista, inicio, fim):
    fim -= 1
    pivor = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivor:
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    print('Merge atual:  {}'.format(lista))
    return i


lenArray = int(input('Informe o tamanho do array: '))
lista = criaVetorEstatico(lenArray)
    
for i in range(0, lenArray):
    lista[i] = int(input('{}° valor: '.format(i + 1)))
print('Lista inicial: {}'.format(lista))
quicksort(lista, 0, lenArray)