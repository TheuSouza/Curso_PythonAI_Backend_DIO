# Operadores Lógicos:

saldo = 1000
saque = 200
limite = 100


# and - As duas condições precisa ser True
saldo >= saque and saque <= limite
# True and False = resultado é False

'''
True = True = True
True = False = False
False = True = False
False = False = False
'''


# or -  Só é necessário que uma das duas condições seja True
saldo >= saque or saque <= limite
# True and False = resultado é True

'''
True = True = True
True = False = True
False = True = True
False = False = False
'''

# not - Inverte o resultado de uma condição 
not saque < limite
# False = not False resultado é True

'''
not True = False
not False = True
'''