# Nesse programa vamos estudar a entrada de números usando
# a função input() e convertendo essa entrada para números.
# A função input sempre recebe uma string (texto), mesmo que 
# um número seja digitado. 

print('=' * 50)
print('----- Somando dois números -----')
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
print(f'Valor da soma: {soma}.')

print('=' * 50)
print('----- Somando dois numeros decimais -----')
numero1 = float(input('Digite um número decimal: '))
numero2 = float(input('Digite outro número decimal:  '))
soma = numero1 + numero2
print(f'Valor da soma: {soma}.')
