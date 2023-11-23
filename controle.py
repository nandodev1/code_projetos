from base import *

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
        maiorAtual = memoria.tamanho
        for part in memoria.particoes:
            if part.tamanho > maiorAtual:
                maiorAtual = part.tamanho

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
        self.alocador.aloca( processo, particoes)

    def proxPasso( self):
        #realiza alocação do processo emlista
        self.alocarProcesso( filaProcesso.pop(), memoria.particoes)
        pass

    def getInfo( self):
        pass
