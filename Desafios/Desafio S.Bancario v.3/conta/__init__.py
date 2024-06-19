from datetime import datetime
import transacoes as trans
import zcores as zc

class Conta:
    def __init__(self, numero, tipo_conta):
        self._saldo = 0
        self._numero = numero
        self._tipo_conta = tipo_conta
        self._agencia = '2325'
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

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f'\n{zc.red()}Operação falhou! Você não tem saldo suficiente.{zc.reset()}')
        
        elif valor > 0:
            self._saldo -= valor
            print(f'\n{zc.green()}Operação realizada com sucesso!{zc.reset()}')
            return True
        
        else:
            print(f'\n{zc.red()}Operação falhou! Valor informado é inválido.{zc.reset()}')
        
        return False
        

    def depositar(self, valor):
        if valor >= 0:
            self._saldo += valor
            print(f'\n{zc.green()}Operação realizada com sucesso!{zc.reset()}')
            return True
        else:
            print(f'\n{zc.red()}Operação falhou! Valor informado é inválido.{zc.reset()}')
        
        return False
   
    
class ContaCorrente(Conta):
    def __init__(self, numero, tipo_conta='001', limite=500, limite_saque=3):
        super().__init__(numero, tipo_conta)
        self._limite = limite
        self._limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self._historico.transacoes
                            if transacao['tipo'] == trans.Saque.__name__])
    
        excedeu_limite = valor > self._limite
        excedeu_limite_saque = numero_saque >= self._limite_saque

        if excedeu_limite:
            print(f'\n{zc.red()}Operação falhou! Você excedeu o limite de saque.{zc.reset()}')
        
        elif excedeu_limite_saque:
            print(f'\n{zc.red()}Operação falhou! Você excedeu o limite de saques diário.{zc.reset()}')
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            tipo:\t{self._tipo_conta}
            Conta:\t\t{self.numero}
            Saldo:\t\t{self._saldo}
  
        '''
    
class ContaPoupanca(Conta):
    def __init__(self, numero, tipo_conta='013', limite=300, limite_saque=3):
        super().__init__(numero, tipo_conta)
        self._limite = limite
        self._limite_saque = limite_saque
    
    def sacar(self, valor):
        numero_saque = len([transacao for transacao in self._historico.transacoes
                            if transacao['tipo'] == trans.Saque.__name__])
    
        excedeu_limite = valor > self._limite
        excedeu_limite_saque = numero_saque >= self._limite_saque

        if excedeu_limite:
            print(f'\n{zc.red()}Operação falhou! Você excedeu o limite de saque.{zc.reset()}')
        
        elif excedeu_limite_saque:
            print(f'\n{zc.red()}Operação falhou! Você excedeu o limite de saques diário.{zc.reset()}')
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            tipo:\t{self._tipo_conta}
            Conta:\t\t{self.numero}
            Saldo:\t\t{self._saldo}

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
    
    def gerar_relatorio(self, contas, tipo_transacao):
        for conta in contas:
            print(f'\nConta N° {conta.numero}', end=(' '))
            print(f'-> {tipo_transacao}')
            print(f'\n\tValor\t\tData\t   Hora')
            for transacao in conta._historico.transacoes:
                if transacao['tipo'] == tipo_transacao:
                    print(f'\tR$:{transacao["valor"]:10.2f}\t{transacao["data"]}')
                elif tipo_transacao == 'Todas transações':
                    print(f'\tR$:{transacao["valor"]:10.2f}\t{transacao["data"]}')
            print('\n')
        