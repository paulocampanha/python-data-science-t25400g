# Nesse programa vamos estudar o escopo de uma variável dentro do 
# programa. Uma variavel declarada fora de qualquer função é 
# considerada um variável global, ou seja, é visível em todo o 
# programa. Uma variável declarada dentro de uma função é considerada 
# uma variável local, ou seja, visível apenas dentro da função.

salario_base = 50.00

def calcular_salario_horista(horas):
    salario_final = horas * salario_base
    return salario_final

def calcular_salario_mensalista(desconto_faltas):
    salario_final = salario_base * 220 - desconto_faltas
    return salario_final

def calcular_salario_vendedor(valor_comissao):
    salario_final = salario_base * 50 + valor_comissao
    return salario_final

funcionario_horista = input('Digite o nome do funcionario horista: ')
horas_trabalhadas = int(input("Quantas horas ele trabalhou? "))
salario_horista = calcular_salario_horista(horas_trabalhadas)
print(f'O salário de {funcionario_horista} é R$ {salario_horista:.2f}.')
print('=' * 50)
funcionario_mensalista = input('Digite o nome do funcionario mensalista: ')
valor_faltas = float(input('Digite o valor de desconto por faltas: '))
salario_mensalista = calcular_salario_mensalista(valor_faltas)
print(f'o salario de {funcionario_mensalista} é R$ {salario_mensalista:.2f}')
print('=' * 50)
vendedor = input('Digite o nome do vendedor: ')
valor_comissao = float(input('Digite o valor da comissao: '))
salario_vendedor = calcular_salario_vendedor(valor_comissao)
print(f'o salario de {vendedor} è R$ {salario_vendedor:.2f}.')
input()