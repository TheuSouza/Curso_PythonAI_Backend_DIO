from time import sleep
import opcao as op
import visual as v
import cores as c
import banco

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
total_deposito = list()
total_saque = list()

clientes = list()
contas = 1

while True:
    opcao = int(input(v.menu1()))
    if opcao == 1:
        banco.cadastro_cliente(clientes)
    elif opcao == 2:
        contas = banco.cadastro_conta(contas, clientes)
    elif opcao == 3:
        for cliente in clientes:
            print(cliente)
    elif opcao == 4:
        break
    else:
        v.header()
        print(f'{c.nred()}Opção inválida!{c.reset()}')
        print(f'{c.yellow()}Por favor selecione uma opção válida.{c.reset()}')
    
    
while True:
    opcao = int(input(v.menu0()))

    if opcao == 1:
        v.sep()
        saldo = op.deposito(saldo, total_deposito)

    elif opcao == 2:
        v.sep()
        saque = float(input('Informe o valor do saque: '))
        saldo, numero_saque = op.saque(
            saldo=saldo, saque=saque, limite=limite, numero_saque=numero_saque, 
            limite_saque=LIMITE_SAQUE, total_saque=total_saque
            )

    elif opcao == 3:
        op.extrato(total_saque, total_deposito, saldo=saldo)
            
    elif opcao == 4:
        op.exit()
        break 

    else:
        v.header()
        print(f'{c.nred()}Opção inválida!{c.reset()}')
        print(f'{c.yellow()}Por favor selecione uma opção válida.{c.reset()}')