# Nesse programa vamos criar um gráfico de barras
import matplotlib.pyplot as plt 

#Dados 
categorias = ["Eletrônicos", "Roupas", "Alimentos", "Livros"]
vendas = [15000, 10000, 20000, 8000]

plt.figure(figsize=(9,6))

plt.bar(categorias, vendas, color=["skyblue", "lightcoral", "lightgreen", "gold"])

plt.title("Vendas Totais por Categoria")
plt.xlabel("Categorias de Produtos")
plt.ylabel("Vendas (R$)")
plt.show()