# Nesse programa vamos estudar funções sem argumento e 
# sem retorno

def linha():
    # Imprimir 50 vezes o '='
    print('=' * 30)
    print()

print('Primeiro programa sobre funções')
linha()
nome = input('Digite seu nome: ')
linha()
idade = int(input('Digite sua idade: '))
linha()
print(f'{nome}, você tem {idade} anos.')
linha()