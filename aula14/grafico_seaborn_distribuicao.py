import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Criando um dataframe
dados = {
    'idade' : [19, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 24, 25, 28, 35]
}

df_alunos = pd.DataFrame(dados)

# Configurando o tema
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df_alunos,
    x='idade',
    kde=True,
    color='darkorange',
    bins=10
)

plt.title('Distribuição de Idade na Turma de Python', fontsize=16)
plt.xlabel('Idade (anos)', fontsize=12)
plt.ylabel('Quantidade de Alunos', fontsize=12)

plt.show()