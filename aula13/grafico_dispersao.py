import matplotlib.pyplot as plt

horas_estudo = [2, 3, 5, 1, 6, 4, 7, 3, 5, 2]
notas_prova = [60, 70, 45, 55, 90, 75, 95, 65, 80, 62]

plt.figure(figsize=(8, 5))
plt.scatter(horas_estudo, notas_prova, 
            color = "red", alpha=0.7)

plt.title("Horas de Estudo vs Nota na prova")
plt.xlabel("Horas de estudo")
plt.ylabel("Hota na prova")

plt.grid(True)
plt.show()