# Nesse programa vamos estudar funções com argumentos
# e sem retorno

# Função para somar dois números
def somar(num1, num2):
    resultado = num1 + num2
    resultado = float(resultado)
    print(f'A soma dos números é {resultado:.2f}')
    print('-' * 50)

# Programa principal
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
somar(numero1, numero2)




