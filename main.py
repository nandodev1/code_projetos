from base import *
import saida

filaProcesso = []
swap = []

global memoria
memoria:Memoria = None


class Controle:
    
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
    def alocarProcesso(  self, Processo) -> bool:
        #verifica setodamemoria está particionada
        pass

    def iniciaAlocador( self):
        pass

    def proxPasso( self):
        pass

    def getInfo( self):
        pass

###################################################################
def main():
    controle = Controle()
    controle.iniciaMemoria(10)
    controle.criaParticao(2)
    controle.criaParticao(5)
    controle.criaParticao(3)
    saida.inprimeMemoria(memoria)
    pass

main()
