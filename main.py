filaProcesso = []
swap = []
# Colunas da tabela inicioParticao, tamParticao, (objeto) processo
tabelaParticao = []

memoria = None

class Particao:
    def __init__( self, inicio:int, tamanho:int, processo:Proce):

# tamanho da memoria é temcomounidade basica kilobytes
class Memoria:
    def __init__( self, tamanhoMemoria:int):
        self.tamanho = tamanhoMemoria

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
        filaProcesso.append(Processo(id, tamanho, nome))
    
    def iniciaMemoria( self, tamanho:int):
        memoria = Memoria(tamanho)

    def iniciaTabelaParticao() -> None:
        pass

    def criParticao(  self, tamanho:int, unidade:str):
        pass

    # Devolve falso caso houver algum erro
    def alocarProcesso(  self, Processo) -> bool:
        #verifica setodamemoria está particionada
        pass

    def iniciaAlocador(self):
        pass

    def proxPasso( self):
        pass

    def getInfo( self):
        pass

###################################################################
def main():
    print(filaProcesso)

main()
