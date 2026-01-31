import matplotlib.pyplot as plt

categorias = ['Livros', 'Roupas','Eletrônicos',  'Alimentos', ]
vendas = [8000,  10000, 15000, 20000, ]


plt.figure(figsize=(9, 6))
plt.barh(categorias, vendas, color=['skyblue', 'lightcoral',
                                'lightgreen', 'gold'])

plt.title("Vendas totais por categorias")
plt.xlabel("Vendas (R$)")
plt.ylabel("Categorias de Produtos")
plt.show()