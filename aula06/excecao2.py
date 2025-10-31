# Nesse programa vamos tratar o erro da dividir um número por 0


try:
    numerador = int(input('Digite um o numerador da divisão: '))
    denominador = int(input('Digite o denominador da divisão: '))

    divisao = numerador / denominador
    print(f'A divisão resultou em {divisao}')
except ZeroDivisionError as e:
    print('Erro: não é possível dividir um número por zero')
    print(f'{e}')
except ValueError as e:
    print('Digite apenas números inteiros')
    print(f'{e}')
except Exception as e:
    print('Erro de sistema. Informe o suporte:')
    print(f'{e}')


