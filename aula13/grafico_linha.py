# Nesse programa vamos criar um simple grafico de linhas

import matplotlib.pyplot as plt

# Criar um figure a um conjunto Axes (área de plotagem)
fig, ax = plt.subplots()

# Dados para o gráfico
ax.plot([1, 2, 3, 4], [10, 42, 23, 35], linestyle=':', 
        marker = "D", color = "#0000ff")

# Rotulos e titulos
ax.set_xlabel("Dias Iniciais")
ax.set_ylabel("Notas")
ax.set_title("Grafico de Notas")
ax.grid(True)

plt.show()