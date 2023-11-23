import base

def inprimeMemoria( memoria:base.Memoria):
    print('-----Memoria--------------------------------------------')
    for i in range(0, len(memoria.particoes)):
        particao = memoria.particoes[i]
        print( '\n--Particao ', i, '----------')
        print( '  inicio:', particao.inicio, 'KB')
        print( '  tamanho:', particao.tamanho, 'KB')
        print('     --processo------------')

        if particao.processo != None:
            print('      Nome: ', particao.processo.nome)
            print('          Id: ', particao.processo.id)
            print('          Tamanho: ', particao.processo.tamanho, 'KB')
        else:
            print('          Livre\n')
    print('--------------------------------------------------------')        
