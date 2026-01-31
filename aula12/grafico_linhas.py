# Nesse programa vamos criar um gráfico de linhas simples
import matplotlib.pyplot as plt

# Dados: Temperaturas diarias durante uma semana em uma região
dias = ["Seg", "Ter", "Qua", "Quin", "Sex", "Sab", "Dom"]
temperaturas = [22, 24, 23, 26, 25, 27, 26]

plt.figure(figsize=(8, 5))  # Cria uma tela (figure) com o tamnho específico em polegadas

plt.plot(dias, temperaturas, marker="D", linestyle="--", color="#00FFFF")

plt.title("Variação da Temperatura Diária na Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Temperatura (C°)")
plt.grid(True)    # Adiciona uma grade na área de plotagem

plt.show()