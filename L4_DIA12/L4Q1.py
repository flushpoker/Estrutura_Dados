def  bemformada(string):
    abertura = [ '(', '[', '{']
    fechamento = [ ')', ']', '}']
    correspondentes = { ')' : '(', ']' : '[', '}' : '{'}
    pilha = []
    for i in string:
        if i in abertura: # se é (, {, [ ou <
            pilha.append(i)
        elif i in fechamento: # se é ), }, ] ou >
            if not pilha: # se a lista está vazia
                return False
            if correspondentes[i] == pilha[-1]:
                pilha.pop()

    return not bool(pilha)


print(bemformada('({(3+2)*{[2+4+5]/(a-y)}}{(t^2)})'))
print(bemformada('{{{{{{{{{{{{{{{{O}}}}}}}}}}}}}}{}}}'))
print(bemformada('asdlkfal{açlsdfjlak]asdjfardfhboi}[()()()(){}{}'))
print(bemformada('{asdfjohs-adslkfgjsk{})({açdsjgfsohjn}}'))