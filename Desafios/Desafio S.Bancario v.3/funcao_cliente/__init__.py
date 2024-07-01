import transacoes as trans
import zcores as zc
import functools
from datetime import datetime

def decorador_log(funcao):
    @functools.wraps(funcao)
    def log(*args, **kwargs):
        funcao(*args, **kwargs)
        print()
        print(f'Data e Hora: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        print()
    return log


@decorador_log
def saque(pessoa_fisica, Pessoa_juridica):
    num_conta = int(input('\nDigite o número da conta: '))
    valor = float(input('Digite o valor do saque: '))

    for cliente in pessoa_fisica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                contador = conta._historico.transacoes_do_dia()
                if contador < 10:
                    transacao = trans.Saque(valor)
                    transacao.registrar(conta)
                continue

    for cliente in Pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                contador = conta._historico.transacoes_do_dia()
                if contador < 10:
                    transacao = trans.Saque(valor)
                    transacao.registrar(conta)
                break


@decorador_log
def deposito(pessoa_fisica, Pessoa_juridica):
    num_conta = int(input('\nDigite o número da conta: '))
    valor = float(input('Digite o valor do deposito: '))

    for cliente in pessoa_fisica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                contador = conta._historico.transacoes_do_dia()
                if contador < 10:
                    transacao = trans.Deposito(valor)
                    transacao.registrar(conta)
                

    for cliente in Pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                contador = conta._historico.transacoes_do_dia()
                if contador < 10:
                    transacao = trans.Deposito(valor)
                    transacao.registrar(conta)
                

@decorador_log              
def extrato(pessoa_fisica, pessoa_juridica):
    num_conta = int(input('\nDigite o número da conta: '))

    for cliente in pessoa_fisica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                saldo = conta.saldo
                print(f'{zc.ncyan()}\nSaldo: {saldo:.2f}{zc.reset()}')
                historico = conta._historico.transacoes
                for c, h in enumerate(historico):
                    print(f'\n{c + 1} ', end=('-> '))
                    for k, v in h.items():
                        if v == 'Saque':
                            print(f'{zc.red()}{k} = {v}{zc.reset()}')
                        elif v == 'Deposito':
                            print(f'{zc.green()}{k} = {v}{zc.reset()}')
                        else:
                            print(f'{k} = {v}')
                        
                        
    
    for cliente in pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                saldo = conta.saldo
                print(f'{zc.ncyan()}\nSaldo: {saldo:.2f}{zc.reset()}')
                historico = conta._historico.transacoes
                for c, h in enumerate(historico):
                    print(f'\n{c + 1} ', end=('-> '))
                    for k, v in h.items():
                        if v == 'Saque':
                            print(f'{zc.red()}{k} = {v}{zc.reset()}')
                        elif v == 'Deposito':
                            print(f'{zc.green()}{k} = {v}{zc.reset()}')
                        else:
                            print(f'{k} = {v}')

