import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset interno do Seaborn
df_tips = sns.load_dataset('tips')
print(df_tips)

# Configurando o estilo visual
sns.set_theme(style="whitegrid")

# Criando o Boxplot
# x: Categoria (Dia da semana)
# y: Variavel numérica (Valor total da conta)
plt.figure(figsize=(10,6))
sns.boxplot(
    data=df_tips,
    x='day',
    y='total_bill',
    palette='Set2'
)

plt.title('Distribuição do Valor das Contas por dia da Semana', fontsize=16)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Valor Total da Conta (R$)', fontsize=12)

plt.show()
