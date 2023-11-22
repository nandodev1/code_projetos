FILA_PROCESSOS = []
SWAP = []

memoria = None

class Processo:
    def __init__(self, id:int, nome:str, tamanho:int):
        self.id = id
        self.nome = nome
        self.tamanho = nome

class Memoria:
    def __init__( self, tamanhoMemoria:int, unidade:str):
        self.tamanho = tamanhoMemoria
        self.unidade = unidade

class TipoAlocacao():
    def __init__(self) -> None:
        pass

        def aloca(self) -> bool:
            pass

class Alocador:
    def __init__( self, algoritimo):
        self.AlgoritimoAlocacao = algoritimo

    def enviaSwap(self):
        pass

    def enviaMemoria(self):
        pass

class Controle:
    
    def criarProcesso(  self, id:str, tamanho:int, nome:str):
        FILA_PROCESSOS.append(Processo(id, tamanho, nome))
    
    # Devolve falso casohouver algum erro
    def alocarProcesso(  self, Processo) -> bool:
        pass

    def iniciaMemoria( self, tamanho:int, unidade:str):
        memoria = Memoria()

    def criParticaoTamParticao(  self, tamanho:int, unidade:str):
        pass

    def iniciaAlocador(self):
        pass

    def proxPasso( self):
        pass

    def getInfo( self):
        pass

###################################################################
def main():
    print(FILA_PROCESSOS)

main()
