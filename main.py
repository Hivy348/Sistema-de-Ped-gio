from veiculos import *
from pedagio import * 
from salvar import salvar_relatorio

# Cria objetos das classes

v1 = Carro(246912,'Cruze',2)
v2 = Caminhao(278093,'Volvo', 4)
v3 = Moto(400323,'Ducati',2)
print(f'O valor fixo do pedágio do Carro é: R$ {v1.calcular_pedagio(): .2f}')
print(f'O valor do pedágio do caminhão é: R$ {v2.calcular_pedagio(): .2f}')
print(f'O valor fixo do pedágio da moto é: R${v3.calcular_pedagio(): .2f}\n') 

# Registra os veículos no pedágio
praca = PracaPedagio()
praca.registrar_veiculo(Carro(246912,'Cruze',2))
praca.registrar_veiculo(Caminhao(278093,'Volvo', 4))
praca.registrar_veiculo(Moto(400323,'Ducati', 2))

praca.mostrar_relatorio()

# Salva o relatório em arquivo .txt
salvar_relatorio(praca)
print('Relatório salvo em relatorio_pedagio.txt!')