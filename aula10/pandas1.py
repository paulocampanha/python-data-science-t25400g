# Nesse programa vamos conhecer as funções básicas da biblioteca
# Pandas
import pandas as pd 
import io

# Simulando a leitura de um arquivo CSV
csv_data = """Produto,Categoria,Preco,Quantidade,DataVenda
Notebook,Eletrônicos,2500.00,1,2025-01-10
Mouse,Acessórios,50.00,2,2025-01-10
Teclado,Acessórios,120.00,1,2025-01-11
Monitor,Eletrônicos,800.00,1,2025-01-11
Fone de Ouvido,Acessórios,80.00,3,2025-01-12
Webcam,Eletrônicos,150.00,1,2025-01-12
Notebook,Eletrônicos,2600.00,1,2025-01-13
Impressora,Eletrônicos,400.00,1,2025-01-13
"""

df_vendas = pd.read_csv(io.StringIO(csv_data))
print("--- DataFrame Original ---")
print(df_vendas)
print("=" * 60)

# Visualizando as primeira linhas do DataFrame
print()
print("--- Primeiras linhas do dataFrame ---")
print(df_vendas.head())
print("=" * 60)

# Visualizando as últimas linhas do dataFrame
print()
print("--- Últimas linhas do DataFrame")
print(df_vendas.tail())
print("=" * 60)

# Visualizando informações do DataFrame(Tipos de dados, 
# valores não nulos)
print()
print("--- Informações do DataFrame ---")
print(df_vendas.info())
print("=" * 60)

# Visualizando a estatística dos dados númericos
print()
print("--- Estatística Descritiva ---")
print(df_vendas.describe())
print("=" * 60)

# Visualizando uma coluna específica (Serie)
print()
print("--- Coluna Produto (Serie) ---")
print(df_vendas["Produto"])
print("=" * 60)

# Visualizando os dados filtrados: categoria Eletrônicos
print()
print("--- Vendas de Eletrônicos ---")
eletronicos = df_vendas[df_vendas['Preco'] == "Eletrônicos"]
print(eletronicos)
print("=" * 60)

# Criar um coluna nova com o valor total de cada linha
print()
print("--- DataFrame com o Valor total ---")
df_vendas['ValorTotal'] = df_vendas['Preco'] * df_vendas['Quantidade']
print(df_vendas)
print("=" * 60)

# Agrupando dados: Vendas total por categoria
print()
print("--- Vendas Totais por Categoria ---")
vendas_por_categoria = \
df_vendas.groupby('Categoria')['ValorTotal'].sum()
print(vendas_por_categoria)
print("=" * 60)

# Converter a coluna 'DataVenda' para o tipo datetime
print()
df_vendas['DataVenda'] = pd.to_datetime(df_vendas['DataVenda'])
print("--- Tipos de dados após a conversão ---")
df_vendas.info()
print("=" * 60)

# Visualizando vendas por data
print()
print("--- Vendas em 10-01-2025 ---")
vendas_dia_10 = df_vendas[df_vendas['DataVenda'] == "2025-01-10"]
print(vendas_dia_10)
print("=" * 60)

# Visualizando em orderm de Preço do menor para o maior
print()
df_ordenado_preco = df_vendas.sort_values(by='Preco')
print("--- DataFrame Ordenado Pelo Preço ---")
print(df_ordenado_preco)
print("=" * 60)

# Visualizando em order de Produto do maior para o menor
print()
df_ordenado_produto = df_vendas.sort_values(by="Produto", 
ascending=False)
print("--- DataFrame Ordenado pelo Produto em ordem decrescente ---")
print(df_ordenado_produto)
print("=" * 60)

# Visualizando a soma, média, valor máximo, valor mínimo e a contagem
# da coluna ValorTotal
print()
print("--- Soma dos Totais ---")
soma_produto = df_vendas.groupby('Produto')['ValorTotal'].sum()
print(soma_produto)
print("=" * 60)
print()
print("--- Média dos Totais ---")
media_categoria = df_vendas.groupby('Categoria')['ValorTotal'].mean()
print(media_categoria)
print("=" * 60)
print()
print("--- Máximo do Total ---")
maximo_categoria = df_vendas.groupby('Categoria')['ValorTotal'].max()
print(maximo_categoria)
print("=" * 60)
print()
print("--- Mínimo do Total ---")
minimo_categoria = df_vendas.groupby('Categoria')['ValorTotal'].min()
print(minimo_categoria)
print("=" * 60)
print()
print("--- Número vendas por Categoria ---")
numero_vendas = df_vendas.groupby("Categoria")['ValorTotal'].count()
print(numero_vendas)
print("=" * 60)


