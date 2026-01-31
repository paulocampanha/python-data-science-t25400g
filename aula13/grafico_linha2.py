import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1, 8)  # [1, 2, 3, 4, 5, 6, 7]
temperaturas = [22, 24, 23, 26, 25, 27, 26]

plt.figure(figsize=(8,5))
plt.plot(dias, temperaturas, linestyle= 'dotted', 
         marker= 's', color='blue')
plt.title("Variação de Temperatura Diária na Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Temperatura (°C)")
plt.grid(True)

plt.show()