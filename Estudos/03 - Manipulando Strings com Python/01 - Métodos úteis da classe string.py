# Conhecendo métodos úteis da classe string:
curso = 'pYtHon AI Backend'

print(curso.upper()) # Coloca toda a string em letras maiúsculas.
print(curso.lower()) # Coloca toda a string em letras minúsculas.
print(curso.capitalize()) # Coloca somente a primeira letra da String em letras maiúsculas.
print(curso.title()) # Coloca todas as primeiras letra de cada palavra da String em letras maiúsculas.
print(curso.count('o')) # Conta quantas letra "x" tem dentro da string.
print(curso.find('o')) # Encontra e mostra o index da primeira letra igual a "x".
print(curso.split()) # Trasforma a string em uma lista separando por padrão onde tem espaços. 
print(curso.split('o')) # Trasforma a string em uma lista separando onde tiver o caractere informado.
print(curso.strip()) # Retira qualquer espaço antes e depois da string.
print(curso.rstrip()) # Retira qualquer espaço depois da string.
print(curso.lstrip()) # Retira qualquer espaço antes da string.
print(curso.replace('o', '*')) # Substitui o valor informado que a string contém pelo novo valor informado.

print(curso.center(10, '-')) # Printa o valor informado com o espaço de 10 caractere se a string for menos, preenche com #####
print('.'.join(curso)) # Join como se fosse um for, interagindo com cada valor da string ou qualquer outro iteravel...


frutas = ['maça', 'banana', 'goiaba', 'laranja', 'abacate', 'carambola']

print(' * '.join(frutas))

text = ' * '.join(frutas).title()

print(text)
