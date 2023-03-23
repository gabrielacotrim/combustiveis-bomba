class combustivel:

    def __init__(self, tipoCombustivel, valorLitro,qntCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qntCombustivel = qntCombustivel
        
    def abastecerPorValor(self, valorAbastecido):
        quantidadeAbastecida = valorAbastecido / self.valorLitro
        return quantidadeAbastecida
    
    def abastecerPorLitro(self, quantidadeLitros):
        totalValor = quantidadeLitros * self.valorLitro
        return totalValor
    
    def alterarValor(self, novoValorLitro):
        self.valorLitro = novoValorLitro
        return novoValorLitro
        
    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        return novoCombustivel
    
    def alterarQuantidadeCombustivel(self, novaQntCombustivel):
        self.qntCombustivel = novaQntCombustivel
        return novaQntCombustivel
               
               