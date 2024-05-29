import visual as v
import re


def cadastro_cliente(clientes):
    usuario = dict()
    v.title('Cadastro')
    print()
    cpf = input('Digite seu CPF: ').strip()
    cpf = re.sub(r'[.,-/_]', '', cpf)
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return print('CPF já cadastrado!')
        else:
            break
    v.sep()
    nome = input('Digite seu nome: ').strip().capitalize()
    v.sep()
    print('Digite data de nascimento [DD/MM/AAAA]: ')
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    v.sep()
    print('Digite seu endereço: ')
    rua = input('Rua: ').strip().capitalize()
    numero = input('Numero: ').strip().capitalize()
    bairro = input('Bairro: ').strip().capitalize()
    cidade = input('Cidade: ').strip().capitalize()
    estado = input('Estado \nExemplo (SP): ').strip().upper()

    usuario['nome'] = nome
    usuario['cpf'] = cpf
    usuario['data_nascimento'] = f'{dia}/{mes}/{ano}'
    usuario['endereco'] = f'{rua}, {numero} - {bairro} - {cidade}/{estado}'
    usuario['contas'] = list()
    clientes.append(usuario)

    return clientes

    

def cadastro_conta(num_contas, clientes):
    resultado = True
    conta = {'conta': str(num_contas), 'agência': '0001'}

    print(f'Conta: {conta["conta"]} \nagência: {conta["agência"]}')
    print(f'Criada com sucesso...')

    cpf = input('Digite o CPF do cliente para vincular conta: ').strip()
    cpf = re.sub(r'[.,-/_]', '', cpf)

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            cliente['contas'].append(conta)
            print('CPF cadastrado, conta vinculada com sucesso!')
            resultado = False
        else:
            continue

    if resultado == True:        
        cadastro_cliente(clientes)
        for cliente in clientes:
            if cliente['cpf'] == cpf:
                cliente['contas'].append(conta)
                print('CPF cadastrado, conta vinculada com sucesso!')
            else:
                continue

    num_contas += 1
    return num_contas

