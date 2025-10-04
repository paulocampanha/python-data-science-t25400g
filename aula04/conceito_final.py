# Nesse programa vamos receber as notas de alguns alunos
# e calcular a média das notas

print('=' * 40)
print('----- Senai Celso Charuri -----')
print('-' * 40)
notas = []
nota = float(input('Digite a uma nota: '))
notas.append(nota)
nota = float(input('Digite a uma nota: '))
notas.append(nota)
nota = float(input('Digite a uma nota: '))
notas.append(nota)
nota = float(input('Digite a uma nota: '))
notas.append(nota)

# Somando os valores da lista
soma_notas = sum(notas)
# Calculado a média das notas
media_notas = soma_notas / len(notas)
print(f'A média das notas foi: {media_notas:.1f}.')
