# Nesse programa vamos trabalhar com um arquivo CSV real para
# explorar a biblioteca Pandas
import pandas as pd 
import io

df_vendas = pd.read_csv('vendas.csv')
print("--- Data Frame Original ---")
print(df_vendas)
print("=" * 60)

# Exercicio
# Imprimir as estatísticas descritiva das vendas
# Imprimir as Vendas do Iphone XS
# Imprimir as Vendas de Televisão
# Criar uma coluna 'Total da Venda' multiplicando o 'Preco' 
# pela 'Quantidade' 
# Imprimir a soma, média, valor máximo, valor mínimo e contagem do
# 'Total da Venda' agrupado por 'Produto'
# Converter a coluna DataVenda para o tipo datetime
# Imprimir as vendas maiores que 01-12-2016
