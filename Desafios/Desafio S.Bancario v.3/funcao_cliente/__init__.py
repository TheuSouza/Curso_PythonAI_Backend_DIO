import transacoes as trans
import zcores as zc

def saque(pessoa_fisica, Pessoa_juridica):
    num_conta = int(input('\nDigite o número da conta: '))
    valor = float(input('Digite o valor do saque: '))

    for cliente in pessoa_fisica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                transacao = trans.Saque(valor)
                transacao.registrar(conta)
                continue

    for cliente in Pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                transacao = trans.Saque(valor)
                transacao.registrar(conta)
                break


def deposito(pessoa_fisica, Pessoa_juridica):
    num_conta = int(input('\nDigite o número da conta: '))
    valor = float(input('Digite o valor do deposito: '))

    for cliente in pessoa_fisica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                transacao = trans.Deposito(valor)
                transacao.registrar(conta)
                

    for cliente in Pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                transacao = trans.Deposito(valor)
                transacao.registrar(conta)
                

                
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
                        

