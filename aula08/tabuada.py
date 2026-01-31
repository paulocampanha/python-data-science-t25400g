# Nesse programa vamos solicitar ao usuário um número para imprtimir
# a tabuada desse número

print("*** Gerador de Tabuadas ***")
print("=" * 30)
numero = int(input("Digite um número para a Tabuada: "))
contador = 1
print("=" * 30)
print(f"Tabuada do {numero}")
print("-" * 30)
while contador <= 10:
    total = numero * contador
    print(f"{numero} X {contador:2} = {total:3}")
    contador += 1             # equivalente à contador = contador + 1

print("=" * 30)
print("Fim da Tabuada")