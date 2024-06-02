class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = list()
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf


class PessoaJuridica(Cliente):
    def __init__(self, endereco, cnpj, razao_social):
        super().__init__(endereco)
        self._cnpj = cnpj
        self._razao_social = razao_social
    
    @property
    def cnpj(self):
        return self._cnpj