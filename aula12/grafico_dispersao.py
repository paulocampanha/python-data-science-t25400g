# Nesse programa vamos criar um gáfico de dispersão
import matplotlib.pyplot as plt

# Dados: Horas de estudo vs. Nota
horas_estudo = [2,3,5,1,6,4,7,3,5,2]
notas_prova = [60, 70,85,55,90, 75,95,65,80,62]

plt.figure(figsize=(8,5))

plt.scatter(horas_estudo, notas_prova, color="red", alpha=0.7)
plt.title("Horas de Estudo vs Nota na Prova")
plt.xlabel("Horas de Estudo")
plt.ylabel("Nota na Prova")
plt.grid(True)
plt.show()

