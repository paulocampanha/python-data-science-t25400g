# As Lojas Malibu estão com uma promoção em todos os eletrodomésticos
# As comprar em até 10 vezes podem ser pagas sem juros. Você foi 
# contrato para criar um programa para ser usado pelo vendedor. Nesse 
# programa, o vendedor deve inserir o nome do produto, o valor do 
# produto, o número de parcelas que o cliente deseja pagar e o melhor
# dia para pagamento entre 5, 10, 15 ou 25. Em seguida seu programa 
# deve imprimir um relatório com as datas de vencimento e o valor de 
# cada parcela, como no exemplo abaixo:
# Produto: Celular - Valor R$ 2000,00 - Parcelas: 4 - Dia Venc: 5
# Relação de Pagamentos
# Parcela 1: 05/12/2025 - R$ 500,00
# Parcela 2: 05/01/2026 - R$ 500,00
# Parcela 3: 05/02/2026 - R$ 500,00
# Parcela 4: 05/03/2026 - R$ 500,00
from datetime import date

nome_produto = input("Digite o nome do Produto: ")
valor_produto = float(input("Digite o valor do Produto: "))
numero_parcelas = int(input("Digite o número de parcelas: "))
valor_parcela = valor_produto / numero_parcelas

dia_pagamento = int(input("Digite o melhor dia para pagamento (5, 10, 15 ou 25)"))

hoje = date.today()
dia = dia_pagamento
mes = hoje.month    # 11
ano = hoje.year     # 2025
contador = 1

while contador <= numero_parcelas:
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
    print(f"Parcela {contador}: {dia}/{mes}/{ano} - R$ {valor_parcela:.2f}")
    contador += 1
