from base import *
import saida

filaProcesso = []
swap = []

global memoria
memoria:Memoria = None


class Controle:
    
    def __init__(self, tipoAlocador:str):
        # Inicializa locador
        self.alocador = Alocador( tipoAlocador)
        self.tamMaiorParticao = None

    def calculaTamMaiorParticao( self):
        maiorAtual = 0
        for part in memoria.particoes:
            if part.tamanho > maiorAtual:
                maiorAtual = part.tamanho
        self.tamMaiorParticao = maiorAtual

    def criarProcesso(  self, id:str, tamanho:int, nome:str):
        #simplifica o uso da fumção pop
        filaProcesso.reverse()
        filaProcesso.append(Processo(id, tamanho, nome))
        filaProcesso.reverse()
    
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
        self.alocador.alocador( processo, particoes, swap)

    def proxPasso( self):
        #realiza alocação do processo emlista
        self.alocarProcesso( filaProcesso.pop(), memoria.particoes)
        pass

    def getInfo( self):
        pass

###################################################################
def main():

    controle = Controle( 'MEA')
    controle.iniciaMemoria(10)
    controle.criaParticao(2)
    controle.criaParticao(5)
    controle.criaParticao(3)

    controle.criarProcesso( 1,'cmd', 5)
    controle.criarProcesso( 2, 'sh',3)
    controle.criarProcesso( 3, 'bash',2)
    controle.criarProcesso( 4, 'cat',4)

    controle.calculaTamMaiorParticao()

    saida.inprimeMemoria(memoria, swap)

    controle.proxPasso()
    controle.proxPasso()
    controle.proxPasso()
    controle.proxPasso()

    saida.inprimeMemoria(memoria, swap)
    
    pass

main()
