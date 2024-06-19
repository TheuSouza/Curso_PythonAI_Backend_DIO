# Estruturas condicionais:
from time import sleep
import sys


saldo = 2000
opcao = int(input('Informe uma opção: [1] Sacar \n[2] Estrato'))

if opcao == 1:
    saque = float(input('Informe o valor do saque: '))
    if saldo >= saque:
        print('\033[36mRealizando saque!')
    if saldo < saque:
        print('\033[34mSaldo insuficientes!')
elif opcao == 2:
    print('Exibindo o estrato...')
    sleep(1.5)
    print(f'Saldo R$:{saldo}')
else:
    sys.exit('\033[31mOpção inválida')