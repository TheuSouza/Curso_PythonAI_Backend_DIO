from pathlib import Path


# Caminho para a pasta de trabalho.
ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / 'novo-diretorio')

try:
    arquivo = open('meu_arquivo.py')
except FileNotFoundError as exc:
    print(f"Arquivo não encontrado...")
    print(exc)

try:
    arquivo = open(ROOT_PATH / 'novo-diretorio')
except IsADirectoryError and PermissionError as exc:
    print(f"O caminho especificado é um diretório...")
    print(exc)