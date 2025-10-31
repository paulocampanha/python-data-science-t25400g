# Nesse programa vamos usar o if ternário para fazer uma comparação
# em única linha


idade = int(input('Digite sua idade: '))

status = "Maior de idade" if idade >= 18 else "Menor idade"

#equivalente a
if idade >= 18:
    status = "Maior de Idade"
else:
    status = "Menor de Idade"