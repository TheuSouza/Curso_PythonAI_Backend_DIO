import transacoes as trans
import conta

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
                continue

    for cliente in Pessoa_juridica:
        for conta in cliente._contas:
            if num_conta == conta._numero:
                transacao = trans.Deposito(valor)
                transacao.registrar(conta)
                break

                
def extrato():
    pass

