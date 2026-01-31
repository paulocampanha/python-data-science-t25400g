import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(12,5))

axs[0].plot([1, 2, 3], [10, 40, 25], color='blue')
axs[0].set_title("Notas Mensais")
axs[0].set_xlabel("Meses")
axs[0].set_ylabel("Notas")

axs[1].bar(["SP","RJ", "MG"], [100, 90, 70], color="orange")
axs[1].set_title("Vendas por Estado")
axs[1].set_xlabel("Estados")
axs[1].set_ylabel("Valores em Milhares")

plt.tight_layout() #Ajusta para caber no layout
plt.show()