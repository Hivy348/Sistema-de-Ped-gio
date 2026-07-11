from veiculos import *
class PracaPedagio:

    def __init__(self):
        self.veiculo = [] 
        self.total_arrecadado = 0
    
    def registrar_veiculo(self,veiculo):

        self.veiculo.append(veiculo) 
        self.total_arrecadado += veiculo.calcular_pedagio()

    def mostrar_relatorio(self):

        print(f' === RELATÓRIO PEDÁGIO ===\n')
        
        for veiculos in self.veiculo:
            print(f'Placa: {veiculos.placa}')
            print(f'Modelo: {veiculos.modelo}')
            print(f'Eixo: {veiculos.eixos}\n')
        
        print(f'Quantidade de veículos presentes: {len(self.veiculo)}\n')
        print(f'Total Arrecadado: R$ {self.total_arrecadado: .2f}\n')