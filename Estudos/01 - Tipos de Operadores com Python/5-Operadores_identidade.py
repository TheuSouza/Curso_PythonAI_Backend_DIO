# Operadores identidade:
# Se as variáveis ocupam o mesmo espaço de memória.

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200


# Curso ocupa o mesmo espaço de nome_curso?
curso is nome_curso

# Curso não ocupa o mesmo espaço de nome_curso?
curso is not nome_curso

# Saldo ocupa o mesmo espaço de saldo?
saldo is limite

