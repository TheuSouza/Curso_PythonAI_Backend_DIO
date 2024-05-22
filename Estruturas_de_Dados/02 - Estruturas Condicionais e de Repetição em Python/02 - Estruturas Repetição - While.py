opcao = None
saldo = 1000

while opcao != 3:
    opcao = int(input(' [1] Saque \n [2] Extrato \n [3] Sair \n Digite a opção desejada:'))
    if opcao == 1:
        saque = float(input('Informe o valor do saque: '))
        if saldo >= saque:
            print('\033[36mRealizando saque!\033[0m')
            print(f'\033[1;31m-{saque}\033[0m')
            saldo -= saque
        else:
            print('\033[31mSaldo insuficientes!\033[0m')
    if opcao == 2:
        print(f'Seu saldo é de R$:\033[1;32m{saldo}\033[0m')
print('\033[1;33mObrigado[a] por ser nosso cliente, Tenha um ótimo dia!\033[0m')


while True: # condição infinita...
    numero = int(input('Digite um numero: '))

    if numero == 10:
        break # força e parada a condição.

    if numero % 2 == 0:
        continue # Serve para pular todo o código a frente e voltar para o loop...