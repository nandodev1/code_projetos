

class Processo:
    def __init__( self, id:int, nome:str, tamanho:int):
        self.id = id
        self.nome = nome
        self.tamanho = tamanho

class Particao:
    def __init__( self, tamanho:int, processo:Processo):
        self.inicio = None
        self.tamanho = tamanho
        self.processo = processo

# tamanho da memoria é temcomounidade basica kilobytes
class Memoria:
    def __init__( self, tamanhoMemoria:int):
        self.tamanho = tamanhoMemoria
        self.particoes:Particao = []

    #Devolve o endereco inicial da partição e Nulo caso não consga alocar partição
    #devido a falta de memoria
    def addParticao(self, particao:Particao) -> int:
        
        #calcula inicio
        soma_tamnho = 0;
        for par in self.particoes:
            soma_tamnho += par.tamanho

        if soma_tamnho + particao.tamanho <= self.tamanho:

            particao.inicio = soma_tamnho
            self.particoes.append(particao)

            if len(self.particoes) == 0:
                return particao.tamamho
            else:
                self.particoes[-1].tamanho + particao.tamanho
        else:
            return None

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
