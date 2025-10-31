# Nesse programa vamos verificar a faixa etária de uma pessoa

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Classificação: infantil')
elif idade <= 17:
    print('Classificação: adolescente')
elif idade <= 64:
    print('Classificação: adulto')
else:
    print('Classificação: idoso')