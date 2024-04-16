from time import sleep


def header():
    print('=' * 50)
    print()


menu = '''
==================================================
MENU:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

Digite a opção desejada:
'''

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
depositos = list()
saques = list()


while True:
    opcao = int(input(menu))

    if opcao == 1:
        while True:
            header()
            deposito = float(input('Informe o valor do deposito: '))
            if deposito <= 0:
                print('\033[34mValor inválido!\nDigite um Valor positivo.\033[0m')
                continue
            depositos.append(deposito)
            saldo += deposito
            sleep(1)
            print(f'\033[1;32mDeposito de R${deposito:.2f} Realizado com Sucesso!\033[0m')
            break

    elif opcao == 2:
        while True:
            header()
            saque = float(input('informe o valor do saque: '))
            if saque > saldo:
                print('\033[1;31mSaldo insuficiente!\033[0m')
                print(f'Saldo da conta R${saldo:.2f}')
                break
            elif numero_saque >= LIMITE_SAQUE:
                print(f'Número de Saque: {numero_saque}\nLimite de Saque: {LIMITE_SAQUE} ')
                print('\033[1;31mLimite de saque excedido!\033[0m')
                break
            elif saque > limite:
                print('\033[1;31mLimite de saque excedido!\033[0m')
                print(f'Limite de Saque R${limite:.2f}')
            else:
                saques.append(saque)
                saldo -= saque
                numero_saque += 1
                sleep(1)
                print(f'\033[1;31mSaque de R${saque:.2f} Realizado com Sucesso!\033[0m')
                print(f'Número de Saque: {numero_saque}\nLimite de Saque: {LIMITE_SAQUE} ')
                break

    elif opcao == 3:
        header()
        print(f'INFORMAÇÃO DA CONTA 001:\n \033[1;36mSaldo R${saldo:.2f}\033[0m')
        print('SAQUES REALIZADOS:')
        for cont, saque in enumerate(saques):
            print(f' {cont + 1} - \033[31mR${saque:.2f}\033[0m')
        print('DEPOSITOS REALIZADOS:')
        for cont, deposito in enumerate(depositos):
            print(f' {cont + 1} - \033[32mR${deposito:.2f}\033[0m')   
            
    elif opcao == 4:
        header()
        print('\033[1;36mObrigado por ser nosso cliente, \ntenha um ótimo dia!\033[0m')
        sleep(0.5)
        print('Saindo...')
        sleep(0.5)
        break 
    else:
        header()
        print('\033[1;31mOpção inválida\033[0m \nPor favor selecione novamente a opção desejada.')