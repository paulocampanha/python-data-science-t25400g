import matplotlib.pyplot as plt
import pandas as pd

df_vendas = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Vendas SP': [100, 120, 150, 130, 160],
    'Vendas RJ': [80, 90, 110, 150, 120 ]
})

plt.figure(figsize=(10, 6))
plt.plot(df_vendas['Mês'], df_vendas['Vendas SP'], 
         label='Vendas SP', marker='o')
plt.plot(df_vendas['Mês'], df_vendas['Vendas RJ'], 
         label='Vendas RJ', marker='x', linestyle='--')

plt.title("Vendas Mensais das lojas de SP e RJ")
plt.xlabel("Meses")
plt.ylabel("Valores em Milhares de Reais")
plt.legend()
plt.grid(True)


plt.savefig("vendas_mensais.png", dpi=300, bbox_inches='tight')
plt.show()
