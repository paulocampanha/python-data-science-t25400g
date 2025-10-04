# Nesse programam vamos solicitar ao usuário a entrada de dois
# números e efetuar algumas operações aritméticas

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
# Operadores aritméticos
# Soma
soma = numero1 + numero2
print(f'A soma dos números é {soma}.')
# Subtração
sub = numero1 - numero2
print(f'A subtração de {numero1} menos {numero2} é {sub}.')
# Multiplicação
multi = numero1 * numero2
print(f'A multiplicação dos números é {multi}.')
# Divisão
# Na divisão o Python sempre converte o resultado para float
div = numero1 / numero2
print(f'A divisão de {numero1} por {numero2} é {div}.')
# Divisão inteira
div_int = numero1 // numero2
# Resto da divisão (modulo)
resto = numero1 % numero2
print(f'O resto da divisão de {numero1} por {numero2} é {resto}')
# Potência
potencia = numero1 ** numero2
print(f'{numero1} elevado a {numero2} é {potencia}')
# Porcentagem
# O python não possui um operador para calcular a porcentagem. Devemos
# utilizar a propria mátemática
# calculando 10% de 500
valor = 500 * 0.1
print(f'10% de 500 é {valor}')
# aumento de 5% sobre 1000
valor = 1000 + (1000 * 0.05)
print(f'Aumento de 5% sobre 1000: {valor}')
# descontando 15% de 2000
valor = 2000 - (2000 * 0.15)
print(f'Desconte de 15% sobre 2000 {valor}')

