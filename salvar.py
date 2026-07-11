from datetime import datetime
from veiculos import *
from pedagio import *

def salvar_relatorio(praca):
    agora  = datetime.now().strftime('%d/%m/%Y  %H:%M:%S')

    with open ("relatorio_pedagio.txt", "w", encoding = "utf-8") as arquivo:
        arquivo.write("=== RELATÓRIO PEDÁGIO === \n")
        arquivo.write(f"Data e hora: {agora} \n")
        arquivo.write("-" * 40 + "\n")

        for veiculos in praca.veiculo:
            arquivo.write(f"Placa: {veiculos.placa}\n")
            arquivo.write(f"Modelo: {veiculos.modelo}\n")
            arquivo.write(f"Eixos: {veiculos.eixos}\n")
            arquivo.write("-" * 40 + "\n")
        arquivo.write(f"Total Arrecadado {praca.total_arrecadado: .2f}\n")
