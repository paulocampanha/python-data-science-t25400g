# Nesse programa vamos fazer o tratamento de dados dupicados
import pandas as pd 

df = pd.read_csv("produtos_com_duplicatas.csv")
print("Dataframe original com dados duplicados")
print(df)
print("=" * 50)
print("\n")

# Removendo todas as linhas duplicadas
df_remover_duplicatas = df.drop_duplicates()
print("Dataframe após remover todas as duplicatas")
print(df_remover_duplicatas)
print("=" * 50)
print("\n")

# Identificar Duplicatas
df_duplicatas = df.duplicated()
print("Valores duplicados (True = duplicado)")
print(df_duplicatas)
print("=" * 50)
print("\n")

# Removendo duplicatas baseadas em um subconjunto
df_remover_duplicatas_sub = df.drop_duplicates(subset=["Produto","Preco"])
print(df_remover_duplicatas_sub)
print("=" * 50)
print("\n")



