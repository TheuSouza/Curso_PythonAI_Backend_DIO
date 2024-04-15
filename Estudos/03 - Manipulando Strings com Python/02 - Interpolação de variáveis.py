nome, idade, profissao, linguagem = 'Matheus', 28, 'Programador', 'Python'


# Print usando modo do Python 2 - não é mais utilizado.
print('Olá, me chamo %s. Tenho %d anos de idade, Trabalho com %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))

# Print .format metodo Python 3 - pouco utilizado.
print('Olá, me chamo {}. Tenho {} anos de idade, Trabalho com {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))

# Print metodo f string modo mais utilizado.
print(f'Olá, me chamo {nome}. Tenho {idade} anos de idade, Trabalho com {profissao} e estou matriculado no curso de {linguagem}')


PI = 3.14159265358979323846

print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:.4f}')
print(f'Valor de PI: {PI:10.2f}')