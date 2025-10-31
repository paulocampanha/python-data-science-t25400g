# Nesse programa vamor ler o conteudo de um arquivo texto usando
# o Python
# 'r' abre um arquivo somente para leitura

def ler_arquivo(nome_arquivo):

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError as e:
        print(f'Arquivo {nomr_arquivo} não encontrado')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')

nome_arquivo = input('Digite o nome do arquivo: ')
ler_arquivo(nome_arquivo)