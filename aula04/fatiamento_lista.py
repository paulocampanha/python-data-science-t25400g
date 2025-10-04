# Nesse programa vamos estudar o fatiamento de lista.
# Nesse caso podemos acessar alguns elementos da lista
# determinando o índice de inicio e o final

# Lista de temperaturas médias na semana
temperaturas = [22, 25, 27, 30, 26, 24, 23]

# Imprimindo a lista completa
print(f'Temperaturas: {temperaturas}')

# Imprindo 3 primeiros dias
print(f'3 primeiros dias: {temperaturas[0:3]}')

# Imprimindo da 2ª até a 4ª temperatura
print(f'Da 2ª a 4ª: {temperaturas[1:4]}')

# Imprimindo as 3 últimas temperaturas
print(f'3 últimos dias: {temperaturas[4:]}')

# Imprindo dia sim, dia não
print(f'Temperaturas alternadas: {temperaturas[::2]}')

# Imprimindo a lista lista invertida
print(f'Lista invertida: {temperaturas[::-1]}')

# Imprimindo útima temperatura
print(f'Útima temperatura: {temperatura[-1]}')
