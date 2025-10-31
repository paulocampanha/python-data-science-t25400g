# Nesse programa vamos calssificar a idade de uma pessoa usando o
# if juntamente com o operador lógico and.

idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade > 12 and idade <= 17:
    print('Adolescente')
elif idade > 17 and idade <= 64:
    print('Adulto')
elif idade < 0:
    print('Idade inválida')
else:
    print('Idoso')