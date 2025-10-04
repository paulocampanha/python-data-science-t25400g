# Nesse programa vamos estudar listas simples e tridimensionais.

# Vetor (listas em Python)
temperaturas_semana = [25, 20.4, 18, 14, 19, 22, 20]

# Lista de responsáveis para sexta, sábado e domingo. 
# responsável, 1º suplente e 2º suplente
# Matriz (lista tridimensional em Python)
lista_responsavel = [
    ['Gaspar', 'Anabela', 'Jorge'],
    ['Anabela', 'Luiza', 'Galego'],
    ['Jorge', 'Galego', 'Luiza']
]

print(f'Temperaturas da semana: {temperaturas_semana}.')
print(f'Temperatura de segunda-feira: {temperaturas_semana[0]}')
print(f'Temperatura do sábado: {temperaturas_semana[5]}')

print(f'Responsáveis pelo restaurante: \n {lista_responsavel}')
print(f'Responsável pela sexta-feira: {lista_responsavel[0][0]}')
print(f'1º suplente de sábado: {lista_responsavel[1][1]}')
print(f'Responsável pelo domingo: {lista_responsavel[2][0]}')


