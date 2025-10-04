# Nesse programa vamos receber 4 notas de um aluno, 
# armazenar em um vetor (lista) e clacular a média 
# das notas

print('----- Escola Senai -----')
print('=' * 50)
notas = []
nota = float(input('Digita a 1ª nota: '))
notas.append(nota)
print(f'Nota adicionada. Notas: {notas}')

nota = float(input('Digite a 2ª nota: '))
notas.append(nota)
print(f'Nota adicionada. Notas: {notas}')

nota = float(input('Digite a 3ª nota: '))
notas.append(nota)
print(f'Nota adicionada. Notas: {notas}')

nota = float(input('Digite a 4 nota: '))
notas.append(nota)
print(f'Nota adicionada. Notas: {notas}')

soma_notas = sum(notas)   # sum() -> soma os itens de uma lista
print(f'Soma das notas: {soma_notas}.')
media = soma_notas / len(notas) 
# len() -> conta quantos itens tem na lista
print(f'A média das notas é: {media}.')

notas[3] = 0
print(f'Maior nota: {max(notas)}.')
print(f'Menor nota: {min(notas)}.')