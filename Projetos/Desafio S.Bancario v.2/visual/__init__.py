def menu0():
    header()
    return '''
    MENU :

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

    => '''

def menu1():
    header()
    return '''
    MENU :

        [1] Cadastrar Usuário
        [2] Cadastrar Conta
        [3] Clientes
        [4] Sair

    => '''

def header():
    print('=' * 50)

def sep():
    print('---')

def title(texto):
    print('=' * 50)
    print(f'{texto:^50}'.upper())
    print('=' * 50)


