import seaborn as sns
import matplotlib.pyplot as plt

# Carregabdo dados do Seaborn
iris = sns.load_dataset('iris')
print(iris)

# Calculando a matriz de correlação
# O método .corr() calcula a relação entre variáveis (de -1 a 1)
# Selecionamos apenas as colunas numéricas para o calculo
correlacao = iris.drop(columns='species').corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlacao,
    annot=True,    # Adiciona os valores dentro dos quadrados
    fmt=".2f",     # Format para 2 casas decimais
    cmap='coolwarm', # Escala de cor (Azul: negativos e Vermelho: positivo)
    linewidths=0.4   # Adiciona uma linha fina entre os quadrados
)

plt.title('Matriz de Correlação - Dataset Iris', fontsize=16)
plt.show()