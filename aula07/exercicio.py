# Faça um programa para calcular o Indice de Massa Corporal (IMC) de
# uma pessoa e imprimir sua classificação de acordo com a tabela 
# abaixo:
# IMC           Classificação
# Abaixo 18.4   Abaixo do Peso Ideal
# 18.5 - 24.9   Peso Normal
# 25 - 29.9     Sobrepeso
# 30 - 34.9     Obesidade Grau I
# 35 - 39.0     Obesidade Grau II
# Acima de 40   Obesidade Grau III
# Formula para calcular o IMC: peso / altura²
# Seu programa deve solicitar do usuário a entrada do peso em quilos 
# e a altura em metros.
# Seu IMC é XX. Sua classificação é: Peso Normal
 
peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do Peso Ideal"
elif imc < 25:
    classificacao = "Peso Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade Grau I"
elif imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III"

print(f"Seu IMC é {imc:.2f}. Sua classificação é: {classificacao}")
