from time import sleep
import cores as c
import visual as v

def deposito(saldo, total_deposito):
    while True:
        deposito = float(input('Informe o valor do deposito: '))
        if deposito <= 0:
            print(f'{c.orange()}Valor inválido!\nDigite um Valor maior que zero.{c.reset()}')
            continue
        total_deposito.append(deposito)
        saldo += deposito
        sleep(1)
        v.sep()
        print(f'{c.ngreen()}Deposito de R${deposito:.2f} Realizado com Sucesso!{c.reset()}')
        break
    return saldo


def saque( * , saldo, saque, limite, numero_saque, limite_saque, total_saque):
    while True:
        saldo_insuficiente = saque > saldo
        limite_saque_diario = numero_saque >= limite_saque
        limite_saque_excedido = saque > limite

        if saldo_insuficiente:
            print(f'{c.red()}Saldo insuficiente!{c.reset()}')
            print(f'Saldo da conta R${saldo:.2f}')
            break

        elif limite_saque_diario:
            print(f'Número de Saque: {numero_saque}')
            print(f'Limite de Saque: {limite_saque}')
            print(f'{c.red()}Limite de saque diário excedido!{c.reset()}')
            break

        elif limite_saque_excedido:
            print(f'{c.red()}Valor do limite de saque excedido!{c.reset()}')
            print(f'Limite de Saque R${limite:.2f}')

        else:
            total_saque.append(saque)
            saldo -= saque
            numero_saque += 1
            sleep(1)
            v.sep()
            print(f'{c.red()}Saque de R${saque:.2f} Realizado com Sucesso!{c.reset()}')
            break
    return saldo, numero_saque

def extrato(total_saque, total_deposito, /, saldo):
        v.header()
        print(f'INFORMAÇÃO DA CONTA:\n {c.ncyan()}Saldo R${saldo:.2f}{c.reset()}')
        print('Saques:')
        for cont, saque in enumerate(total_saque):
            print(f' {cont + 1} - {c.red()}R${saque:.2f}{c.reset()}')
        print('Depositos:')
        for cont, deposito in enumerate(total_deposito):
            print(f' {cont + 1} - {c.green()}R${deposito:.2f}{c.reset()}') 

def exit():
    v.header()
    print(f'{c.yellow()}Obrigado por ser nosso cliente{c.reset()}')
    print(f'{c.ncyan()}tenha um ótimo dia!{c.reset()}')
    sleep(0.5)
    print('Saindo...')
    sleep(0.5)