# Nesse programa vamos ler o conteude de um arquivo csv

def ler_arquivo(nome_arquivo):

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print('=' * 50)
            print(conteudo)
            print('=' * 50)
    except FileNotFoundError:
        print(f'Erro ao abrir o arquivo {nome_arquivo}')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')

nome_do_arquivo = 'relatorio.csv'
ler_arquivo(nome_do_arquivo)