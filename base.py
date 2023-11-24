

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

# Detecção defragmentação externa
# Para enviar processo para o swap
class Alocador:

    def __init__( self, algoritimo:str):
        self.algoritimoAlocacao = algoritimo

    def aloca(self, processo:Processo, particoes):
        
        if self.algoritimoAlocacao == 'PEA':
            for par in particoes:
                if par.processo == None and par.tamanho >= processo.tamanho:
                    par.processo = processo
                    break
        #escolhe a partição que resultará na menor fragmentação esterna
        if self.algoritimoAlocacao == 'MEA':
            melhorEscolha = self.particaoMath(particoes, processo)
            particoes[melhorEscolha].processo = processo


    def particaoMath(self, particoes, processo:Processo) -> int:
        menor_particao = 99999
        particaoMelhor:int = None
        
        for i in range( 0, len(particoes)):
            sobraParticaoAtual = particoes[i].tamanho - processo.tamanho 
            if sobraParticaoAtual >= 0 and sobraParticaoAtual < menor_particao and particoes[i].processo == None:
                menor_particao = sobraParticaoAtual
                particaoMelhor = i

        return particaoMelhor      

    def enviaSwap(self):
        pass

    def enviaMemoria(self):
        pass
