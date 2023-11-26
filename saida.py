import base

def inprimeMemoria( memoria:base.Memoria, swap):
    print('-----Memoria--------------------------------------------')
    for i in range(0, len(memoria.particoes)):
        particao = memoria.particoes[i]
        print( '##############################')
        print( '\n--Particao ', i, '----------')
        print( '  inicio:', str(particao.inicio) + 'K')
        print( '  tamanho:', str(particao.tamanho) + 'K')

        if particao.processo != None:
            print( '  Fragmentação Interna:', str(particao.tamanho - particao.processo.tamanho) + 'K')
            imprimeDadosProcesso( particao.processo)
        else:
            print('          LIVRE\n')

    print( '##############################')
    imprimeSwap( swap)
    print('--------------------------------------------------------')
     
def imprimeDadosProcesso( processo):
    print('--------processo-------------')
    print('      Nome: ', processo.nome)
    print('          Id: ', processo.id)
    print('          Tamanho: ', str(processo.tamanho) + 'K')

def imprimeSwap(swap):
    print('++++++++++++++++++++++++++++++')
    print( 'SWAP')
    for proc in swap:
        print('++++++++++++++++++++++++++++++')
        imprimeDadosProcesso(proc)
        print('++++++++++++++++++++++++++++++')