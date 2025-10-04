# Nesse programa vamos estudar matrizes. Uma matriz
# é uma lista com outras listas separadas por linhas.
# cada linha representa uma lista

# Matriz de vendas dos 3 vendedores nos últimos 4 meses

vendas = [
    [100, 150, 110, 180],      # Vendas do 1º vendedor
    [90, 140, 120, 170],       # Vendas do 2º vendedor
    [110, 160, 130, 190]       # Vendas do 3º vendador
]

print(f'Vendas totais: {vendas}')

print(f'Vendas do Gaspar: {vendas[0]}')
print(f'Vendas da Luiza do 2º mês {vendas[1][1]}')

media_vendedor1 = sum(vendas[0]) / len(vendas[0])
media_vendedor2 = sum(vendas[1]) / len(vendas[1])
media_vendedor3 = sum(vendas[2]) / len(vendas[2])

print(f'Media das vendas do Gaspar: {media_vendedor1:.2f}.')
print(f'Media das vendas da Luiza: {media_vendedor2:.2f}.')
print(f'Media das vendas do Jorge: {media_vendedor3:.2f}.')

soma_vendas = sum(vendas[0]) + sum(vendas[1]) + sum(vendas[2])
meses = len(vendas[0]) + len(vendas[1]) + len(vendas[2])
media_vendas = soma_vendas / meses
print(f'Média das vendas: {media_vendas:.2f}.')
