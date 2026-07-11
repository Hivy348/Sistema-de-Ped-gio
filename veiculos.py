class Veiculo:

    def __init__(self,placa,modelo,eixos):
        self.placa = placa
        self.modelo = modelo
        self.eixos = eixos

    def calcular_pedagio(self):
       pass

# Subclasse Carro
class Carro(Veiculo):

    def __init__(self,placa,modelo,eixos):
        super().__init__(placa,modelo,eixos)

    def calcular_pedagio(self):
        return 12.00
    
# Subclasse Moto
class Moto(Veiculo):

    def __init__(self, placa, modelo, eixos):
        super().__init__(placa, modelo, eixos)
    
    def calcular_pedagio(self):
        return 6.00

# Subclasse Caminhão
class Caminhao(Veiculo):

    def __init__(self, placa, modelo,eixos):
        super().__init__(placa, modelo, eixos)

    def calcular_pedagio(self):
        return self.eixos * 10.00
    