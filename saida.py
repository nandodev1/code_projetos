import base

def inprimeMemoria( memoria:base.Memoria, swap):
    print('-----Memoria--------------------------------------------')
    for i in range(0, len(memoria.particoes)):
        particao = memoria.particoes[i]
        print( '##############################')
        print( '\n--Particao ', i, '----------')
        print( '  inicio:', str(particao.inicio) + 'K')
        print( '  tamanho:', str(particao.tamanho) + 'K')
        print('--------processo-------------')

        if particao.processo != None:
            imprimeDadosProcesso( particao.processo)
        else:
            print('          Livre\n')

    print( '##############################')
    imprimeSwap( swap)
    print('--------------------------------------------------------')
     
def imprimeDadosProcesso( processo):
    print('      Nome: ', processo.nome)
    print('          Id: ', processo.id)
    print('          Tamanho: ', str(processo.tamanho) + 'K')

def imprimeSwap(swap):
    print( 'SWAP')
    for proc in swap:
        print('++++++++++++++++++++++++++++++')
        imprimeDadosProcesso(proc)
        print('++++++++++++++++++++++++++++++')