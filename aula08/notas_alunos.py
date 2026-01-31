
soma_notas = 0
media = 0
nota = 0
contador = 0

while True:
    nota = float(input("Digite a nota do aluno: "))
    contador += 1
    soma_notas += nota
    resposta = input("Deseja digitar outra nota S/N: ")
    if resposta.upper() == "N":
        break

media = soma_notas / contador
print(f"A media do aluno foi {media:.1f}")