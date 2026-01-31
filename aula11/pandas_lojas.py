import pandas as pd

df = pd.read_csv("vendas_lojas.csv")

print("--- DataFrame Original ---")
print(df)
print("-" * 50)

# Visualizando as primeiras linhas
print("--- Primeiras Linhas ---")
print(df.head(20))
print("-" * 50)

# Visualizando as últimas linhas
print("--- Últimas Linhas ---")
print(df.tail(20))
print("-" * 50)

# Visualizando informações do DataFrame
print("--- Informações do DataFrame ---")
print(df.info())
print("-" * 50)

# Visualizando Descrição estatística
print("--- Descrição Estatística ---")
print(df.describe())
print("-" * 50)

# Visualizando Uma coluna específica
print("--- Coluna 'Marca' (Series) ---")
print(df["Marca"].head(20))
print("-" * 50)

# Filtrando Dados
print("--- Vendas de Notebooks ---")
notebooks = df["Categoria"] == "Notebook"
print(df[notebooks])
print("-" * 50)

# Filtrando Dados pelo preco unitario
print("--- Vendas de abaixo de R$ 1.000,00 ---")
vendas_menor_1000 = df["Preço Unitário"] <= 1000
print(df[vendas_menor_1000])
print("-" * 50)

# Convertendo a coluna 'Data da Venda' para o tipo datatime
df["Data da Venda"] = pd.to_datetime(df["Data da Venda"])
print("--- Tipo de dados após a conversão ---")
print(df.info())
print("-" * 50)

# Filtrando vendas por data
print("--- Vendas em 2016-01-10 ---")
vendas_dia_10_01 = df["Data da Venda"] == "2016-01-10"
print(df[vendas_dia_10_01])
print("-" * 50)

# Filtrando o ano de 2017
print("--- Vendas em 2017 ---")
filtro_ano_2017 = df["Data da Venda"].dt.year == 2017
print(df[filtro_ano_2017])
print("-" * 50)

# Filtrando o mes 7 de 2016
print("--- Vendas de julho  de 2016 ---")
filtro_ano = df["Data da Venda"].dt.year == 2016
filtro_mes = df["Data da Venda"].dt.month == 7
vendas_mes_ano = df[filtro_ano & filtro_mes]
print(vendas_mes_ano)
print("-" * 50)

# Filtrando as vendas de janeiro a junho de 2018
print("--- Vendas de Janeiro a Junho de 2018 ---")
data_inicial = df["Data da Venda"] >= "2018-01-01"
data_final = df["Data da Venda"] <= "2018-06-30"
vendas_periodo = df[data_inicial & data_final]
print(vendas_periodo)
print("-" * 50)

# Criando uma coluna nova de Total da Venda
df["Total da Venda"] = df["Preço Unitário"] * df["Tamanho Pedido"]
print("--- DataFrame com Totad da Venda ---")
print(df)
print("-" * 50)

# Agrupando dados por categoria
print("--- Vendas Totais por Categoria ---")
vendas_por_categoria = df.groupby("Categoria")["Total da Venda"].sum()
print(vendas_por_categoria)
print("-" * 50)










