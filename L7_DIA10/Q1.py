class NoArvoreAVL:
    def __init__(self, chave, dado, altura=1, alturaEsquerda=0, alturaDireita=0, fatorBalanceamento=0, pai=None, esquerda=None, direita=None):
        self.chave = dado
        self.dado = dado
        self.altura = altura
        self.alturaEsquerda = alturaEsquerda
        self.alturaDireita = alturaDireita
        self.fatorBalanceamento = fatorBalanceamento
        self.pai = pai #NoArvoreAVL
        self.esquerda = esquerda #NoArvoreAVL
        self.direita = direita #NoArvoreAVL

class ArvoreAVL:
    def __init__(self, raiz=None):
        self.raiz = raiz #NoArvoreAVL

def impressaoAVL(no_raiz):
    if no_raiz.esquerda:
        impressaoAVL(no_raiz.esquerda)
    print('{} ({})'.format(no_raiz.dado, no_raiz.fatorBalanceamento), end=' ')
    impressao = (str(no_raiz.dado) + ' (' + str(no_raiz.fatorBalanceamento) + ') ')
    arquivo_out.write(impressao)
    if no_raiz.direita:
        impressaoAVL(no_raiz.direita)

def inserirArvoreBin(no_arvore, raiz):
    pai = None
    raiz_arvore = raiz.raiz
    while raiz_arvore != None:
        pai = raiz_arvore
        if no_arvore.chave <= raiz_arvore.chave:
            raiz_arvore = raiz_arvore.esquerda
        else:
            raiz_arvore = raiz_arvore.direita

    no_arvore.pai = pai
    if pai == None:
        raiz.raiz = no_arvore
    elif no_arvore.chave <= pai.chave:
        pai.esquerda = no_arvore
    else:
        pai.direita = no_arvore

def inserirArvoreAVL(no_arvore, raiz):
    inserirArvoreBin(no_arvore, raiz)
    eAVL = verificarBalanceamentoNo(no_arvore)

    if eAVL:        
        return raiz
    else:
        pass

def verificarBalanceamentoNo(no_arvore):
        
    if no_arvore == None: 
        arquivo_out.write('arvore ja balanceada.\n')
        print('arvore ja balanceada.')
        return False
    else:
        CalcularFatorBalanceamento(no_arvore)
        if no_arvore.fatorBalanceamento < -1 or no_arvore.fatorBalanceamento > 1:
            if no_arvore.fatorBalanceamento > 1:
                arquivo_out.write('rotacao a direita.\n')
                print('rotação a direita.')
                #falta implementar as rotações
                pass

            if no_arvore.fatorBalanceamento < -1:
                arquivo_out.write('rotacao a esquerda.\n')
                print('rotação a esquerda.')
                #falta implementar as rotações
                pass
            return True
        else:
            no_arvore = no_arvore.pai
            
            return verificarBalanceamentoNo(no_arvore)
    
def CalcularFatorBalanceamento(no_arvore):
    if no_arvore.direita:
        no_arvore.alturaDireita = no_arvore.direita.altura
    else:
        no_arvore.alturaDireita = 0
    if no_arvore.esquerda:
        no_arvore.alturaEsquerda = -1
    else:
        no_arvore.alturaEsquerda = 0

    no_arvore.fatorBalanceamento = no_arvore.alturaDireita - no_arvore.alturaEsquerda

    no_arvore.altura = max(no_arvore.alturaDireita, no_arvore.alturaEsquerda) + 1
    
def max(param_1, param_2):
    if param_1 >= param_2:
        return param_1
    else:
        return param_2


menu = -1
raiz = ArvoreAVL(None)

arquivo_in = open('E:\Documentos\Visual Studio\python\Estrutura_Dados\L7_DIA10\L7Q1_in.txt', 'r')
arquivo_out = open('E:\Documentos\Visual Studio\python\Estrutura_Dados\L7_DIA10\L7Q1_out.txt', 'w')
i = 0
dadoArquivo = ''
    
for linha in arquivo_in:
    dadoArquivo = linha.split()
    for ii in range(0, len(dadoArquivo)):
        no_arvore = NoArvoreAVL(i, dadoArquivo[ii])
        inserirArvoreAVL(no_arvore, raiz)
        impressaoAVL(raiz.raiz)
        print('\n{}'.format(raiz.raiz.altura))
        arquivo_out.write('\n' + str(raiz.raiz.altura) + '\n')
        i += 1
    arquivo_out.write('\n')
    print('')
    raiz = ArvoreAVL(None)
    i = 0
