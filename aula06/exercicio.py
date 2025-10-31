# Desenvolva um programa que criar um arquivo texto com o nome de
# poema.txt. 
# Solicite ao usuário (input) para digitar uma frase e grave no 
# arquivo.
# Leia o arquivo criado e imprima o conteudo no console.
# Para esse exercício crie duas funções:
# gravar_arquivo -> esse função recebe o nome do arquivo e o texto e
# grava esse texto no arquivo.
# imprimir_arquivo -> esse função lê o conteúdo do arquivo e imprime
# seu conteudo no console.

def gravar_arquivo(nome_arquivo, texto):
    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(texto)
    except Exception as e:
        print(f'Erro: {e}')

nome_do_arquivo = 'poema.txt'
texto = input('Digite o seu poema; ')
gravar_arquivo(nome_do_arquivo, texto)