import base

def inprimeMemoria( memoria:base.Memoria):
    for i in range(0, len(memoria.particoes)):
        particao = memoria.particoes[i]
        print( '--Particao ', i, '----------')
        print( '  inicio:', particao.inicio, 'kB')
        print( '  tamanho:', particao.tamanho, 'kB')
        print('     --processo------------')

        if particao.processo != None:
            print('    ', particao.processo)
        else:
            print('          Livre\n')
        
