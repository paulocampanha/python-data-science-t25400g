# Nesse programa vampos fazer o tratamento de dados não padronizados
import pandas as pd 

df = pd.read_csv("paises_inconsistentes.csv")
print("Dataframe original com inconsistência de dados")
print(df)
print("=" * 50)
print("\n")

print("Contagem de valores únicos:")
print(df['Pais'].value_counts())
print(df['Status'].value_counts())
print("=" * 50)
print("\n")

print("Converter para minúsulas e remover espaços em branco")
df["Pais"] = df["Pais"].str.lower().str.strip()
df["Status"] = df["Status"].str.lower().str.strip()
print(df)
print("=" * 50)
print("\n")

print("Converter a primeira letra para maiúscula")
df["Pais"] = df["Pais"].str.capitalize()
df["Status"] = df["Status"].str.upper()
print(df)
print("=" * 50)
print("\n")