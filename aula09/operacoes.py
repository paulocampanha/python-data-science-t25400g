# Nesse programa vamos efetuar algumas operações matemáticas
import numpy as np


vendas = np.array([100, 270, 160, 190, 150, 200])
taxa = 0.1  # 10% de imposto

# aplicando o imposto
vendas_com_imposto = vendas * (1 + taxa)
valor_imposto = vendas * taxa

print(f"Vendas: {vendas}")
print(f"Imposto: {valor_imposto}")
print(f"Vendas com imposto: {vendas_com_imposto}")

vendas_ordenadas = np.sort(vendas)
print(f"Vendas Ordenadas: {vendas_ordenadas}")

# Funções de estatística
print(f"Total das Vendas: {vendas.sum()}")
print(f"Média de Vendas: {vendas.mean()}")
print(f"Desvio Padrão das Vendas: {vendas.std()}")
 

