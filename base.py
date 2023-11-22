FILA_PROCESSOS = []
SWAP = []

class Processo:
    def __init__(self, id:int, nome:str, tamanho:int):
        self.id = id
        self.nome = nome
        self.tamanho = nome

class Memoria:
    def __init__( self, tamanhoMemoria, tamanhoParticao):
        self.tamanho = tamanhoMemoria
        self.tamanhoParticao = tamanhoParticao
        
class Alocador:
    def __init__( self, algoritimo):
        self.AloritimoAlocacao = algoritimo

    def enviaSwap(self):
        pass

    def enviaMemoria(self):
        pass
