# Nesse programa vamos trabalhar com tratamento de erros

try:
    idade = int(input('Digite sua idade: '))

    print(f'Sua idade é {idade}')
except ValueError as e:
    print(f'Erro: Digite apenas números inteiros.')
    print(f'{e}')