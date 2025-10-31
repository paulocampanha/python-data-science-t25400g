# Nesse programa vamos receber 3 notas entre 0 e 100, calcular 
# a média e verificar se o aluno está aprovado ou reporvado. 
# Para ser aprovado o aluno precisa de méia igual ou superior a 50

print('=' * 30)
print('Escola Senai')
print('=' * 30)
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 50:
    print(f'O aluno {nome} está APROVADO')
else:
    print(f'O aluno {nome} está REPROVADO')

print(f'Sua média foi {media:.1f}')
print('=' * 30)