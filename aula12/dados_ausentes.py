# Nesse programa vamos fazer o tratamento de dados ausente
import pandas as pd

df = pd.read_csv("clientes_ficticios.csv")
print("=" * 40)
print("*** Base Original ***")
print(df)
print("=" * 40)
print("\n")

# Identificar dados ausentes
print("=" * 50)
print("Valore Ausentes por coluna (True = Ausente)")
print(df.isna())
print("=" * 50)
print("\n")

# Contagem de valores ausente
print("Contagem de valores ausente")
print(df.isna().sum())
print("=" * 50)
print("\n")

# Estratégia A: Removendo as linhas com qualquer valor ausente
df_linhas_removidas = df.dropna()
print('Dataframe com linhas Removidas')
print(df_linhas_removidas)
print("=" * 50)
print("\n")
clientes_removidos = "clientes_removidos.csv"
df_linhas_removidas.to_csv(clientes_removidos, index=False)

# Estrategia B: Preeencher valores ausentes
# Preencher a Idade com a media das idades
df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
# Prencher a Cidade com valor padrão: 'Desconhecida'
df['Cidade'] = df['Cidade'].fillna('Desconhecida')
# Preencher a Renda com a Mediana
df['Renda'] = df['Renda'].fillna(df["Renda"].median())

print("Dataframe com dados ausentes preenchidos")
print(df)
print("=" * 50)
print("\n")

clientes_preenchidos = "clientes_preenchidos.csv"
clientes_preenchidos_excel = "clientes_preenchidos.xlsx"
df.to_csv(clientes_preenchidos, index=False)
df.to_excel(clientes_preenchidos_excel, index=False, engine='xlsxwriter')


