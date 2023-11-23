from base import *
import saida

filaProcesso = []
swap = []

global memoria
memoria:Memoria = None


class Controle:
    
    def __init__(self):
        # Inicializa locador
        self.alocador = Alocador( 'FSR')

    def criarProcesso(  self, id:str, tamanho:int, nome:str):
        filaProcesso.append(Processo(id, tamanho, nome))
    
    def iniciaMemoria( self, tamanho:int):
        global memoria
        memoria = Memoria(tamanho)
    #tamanho em kilobyte
    #erro ocorre com retorno diferentede zero
    # Devolve -1 caso memoria não inicializada
    def criaParticao( self, tamanho:int) -> int:
        #verifica tamanhodamemoriafisicajá definido
        if memoria == None:# Memoria fi inicializada
            return -1
        
        memoria.addParticao(Particao( tamanho, None))

        return 0

    # Devolve falso caso houver algum erro
    def alocarProcesso(  self, processo: Processo, particoes) -> bool:
        self.alocador.aloca( processo, particoes)

    def proxPasso( self):
        pass

    def getInfo( self):
        pass

###################################################################
def main():
    controle = Controle()
    controle.iniciaMemoria(15)
    controle.criaParticao(2)
    controle.criaParticao(5)
    controle.criaParticao(3)
    controle.criaParticao(4)
    controle.criaParticao(1)

    filaProcesso.append( Processo( 1,'cmd', 5), memoria.particoes)
    filaProcesso.append( Processo( 2,'sh', 3), memoria.particoes)

    saida.inprimeMemoria(memoria)

    

    saida.inprimeMemoria(memoria)
    
    pass

main()
