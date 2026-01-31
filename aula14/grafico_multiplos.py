import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Mês' : ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
    'Vendas' : [1500, 1800, 2200, 2500, 2100, 2800, 3100, 2900, 3500, 3800, 3100, 4500],
    'Volume' : [50, 65, 80, 95, 75, 110, 120, 105, 135, 150, 113, 200],
    'Margem' : [0.15, 0.18, 0.20, 0.19, 0.17, 0.22, 0.25, 0.23, 0.26, 0.28, 0.24, 0.32],
    'Filial' : ['SP', 'RJ', 'SP', 'MG', 'RJ', 'SP', 'MG', 'RJ', 'SP', 'MG', 'RJ', 'SP']
}

df = pd.DataFrame(data)

# Gráfico de Linhas (Tendência mensal)
plt.figure(figsize=(10, 6))

# Plotar os dados
plt.plot(
    df['Mês'], 
    df['Vendas'],
    marker = 'o',
    linestyle = '-',
    color = 'blue',
    label = 'Vendas Totais'
)

# Titulos e formatações
plt.title('Tendência de Vendas Mensais (R$)', fontsize=16)
plt.xlabel("Meses", fontsize=12)
plt.ylabel('Valor Total de Vendas (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Salvando o grafico em arquivo png
plt.savefig('tendencia_vendas_linha.png')

# Grafico de Barras (Comparação categórica)
plt.figure(figsize=(10, 6))

plt.bar(
    df['Mês'],
    df['Volume'],
    color=['gray', 'red','gray', 'red','gray', 'red','gray', 'red','gray', 'red','gray', 'red']
)

plt.title('Volume de Unidades Vendidas por Mês', fontsize=16)
plt.xlabel('Meses', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)

# Adiciona rótulo de dados em cima das barras
for i in range(len(df['Mês'])):
    plt.text(i, df['Volume'][i] + 3, str(df['Volume'][i]), ha='center')

plt.savefig('volume_barras.png')

# Gráfico de dispersão (Relação entre variáveis)

plt.figure(figsize=(8, 8))

plt.scatter(
    df['Volume'],
    df['Vendas'],
    c= 'red',
    s=df['Margem'] * 2000, 
    alpha=0.7
)

plt.title('Relação entre volume e vendas', fontsize=16)
plt.xlabel('Volume de unidades', fontsize=12)
plt.ylabel('Valor de vendas (R$)', fontsize=12)

plt.savefig('relacao_volume_vendas_dispersas.png')

plt.show()



