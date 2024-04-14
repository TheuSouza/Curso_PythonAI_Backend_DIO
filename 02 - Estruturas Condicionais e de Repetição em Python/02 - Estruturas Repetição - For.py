from time import sleep


texto = input('Digite seu texto: ').strip()
VOGAIS = 'AEIOU'


# exemplo utilizando iterável...
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f'\033[1;36m{letra}\033[0;0m', end='')
    else:
        print(letra, end='')
else: # pouco usável mas exite.
    print()
    print('Fim do código...')


# exemplo utilizando a função built-in range...
for numero in range(0, 10, 2):
    print(numero, end=' ')
    sleep(0.5)