from datetime import datetime

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\nOperação falhou! Você não tem saldo suficiente.')
        
        elif valor > 0:
            self._saldo -= valor
            print('\nOperação realizada com sucesso!')
            return True
        
        else:
            print('\nOperação falhou! Valor informado é inválido.')
        
        return False
        

    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
            print('\nOperação realizada com sucesso!')

        else:
            print('\nOperação falhou! Valor informado é inválido.')
   
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self.historico.transacoes
                            if transacao['tipo'] == Saque.__name__])
    
        excedeu_limite = valor > self._limite
        excedeu_limite_saque = numero_saque >= self._limite_saque

        if excedeu_limite:
            print('\nOperação falhou! Você excedeu o limite de saque.')
        
        elif excedeu_limite_saque:
            print('\nOperação falhou! Você excedeu o limite de saques diário.')
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''
        

class Historico():
    def __init__(self):
        self._transacoes = list()
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adcionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
        )
        