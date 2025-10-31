# Nesse programa vamos verificar se o aluno é menor de idade


print('=' * 30)
print('Escola Senai')
print('=' * 30)
nome_aluno = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))

if idade < 18:
    print('Seu pai ou responsável deve estar presente para a matrícula')

print('Dirija-se ao balcão da secretaria para matrícula no curso.')