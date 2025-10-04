# IMC é o indice de massa corporal que mede se uma pessoa
# está com seu peso ideal.
# Crie um programa que solicita ao usuário o seu peso em 
# quilos (exemplo: 65.5) e sua altura em metros (exemplo: 1.75)
# Calcule e imprima no console o IMC dessa pessoa com uma casa
# decimal.
# Formula para calcular o IMC 
# imc = peso / (altura * altura) ou
# imc = peso / altura ** 2
# Dica: para imprimir com uma casa decimais use o f-string e
# {imc:.1f} 

peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print(f'Seu IMC é {imc:.1f}')

