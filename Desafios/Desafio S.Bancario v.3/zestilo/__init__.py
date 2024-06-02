from time import sleep
import zcores as zc


def menu0():
    menu = '''
    MENU :

        [1] Função Gerente
        [2] Função Cliente
        [3] Sair

    => '''
    sep()
    return int(input(menu))

def menu1():
    menu = '''
    Funções Cliente :

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Retornar ao Menu anterior

    => '''
    sep()
    return int(input(f'{zc.yellow()}{menu}{zc.reset()}'))

def menu2():
    menu = '''
    Funções Gerente :

        [1] Cadastrar Usuário
        [2] Cadastrar Conta
        [3] Clientes
        [4] Retornar ao Menu anterior

    => '''
    sep()
    return int(input(f'{zc.orange()}{menu}{zc.reset()}'))

def menu3():
    menu = '''
    Cadastrar Usuário:

        [1] Pessoa Física
        [2] Pessoa Jurídica
        [3] Retornar ao Menu anterior

    => '''
    sep()
    return int(input(f'{zc.cyan()}{menu}{zc.reset()}'))

def header():
    print('=' * 50)

def sep():
    print()
    print('-' * 50)

def title(texto):
    print('=' * 50)
    print(f'{texto:^50}'.upper())
    print('=' * 50)

def bem_vindo():
    title('banco iteuz')
    print(f'{zc.magenta()}\nBem vindo ao Sistema Bancário{zc.reset()}')
    sleep(1)
    print(f'{zc.magenta()}Escolha uma das opções abaixo:{zc.reset()}')
    sleep(1)

def erro():
    print(f'{zc.red()}\nOpção inválida!{zc.reset()}')
    print(f'{zc.red()}Por favor selecione uma opção válida.{zc.reset()}')
    sleep(1)

