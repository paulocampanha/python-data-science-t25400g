# Nesse programa vamos imprimir uma sequencia mensal de datas a
# partir da data atual

from datetime import date
hoje = date.today() # Obtém a data atual do sistema
print(f"Hoje é {hoje}")
# Atribiu cada parte da data a uma variável
dia = hoje.day
mes = hoje.month
ano = hoje.year

contador = 1

while contador <= 24:
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
    print(f"{dia:02}/{mes:02}/{ano}")
    contador += 1
