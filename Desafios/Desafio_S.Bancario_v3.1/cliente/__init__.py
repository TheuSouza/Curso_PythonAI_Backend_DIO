class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = list()

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    def __repr__(self):
        return f'{self.__class__.__name__}: {self._cpf}'
    
    def __str__(self):
        return f'''
        Nome:{self._nome}
        CPF:{self._cpf}
        Data de Nascimento:{self._data_nascimento}
        Endereço:{self._endereco}
    '''


class PessoaJuridica(Cliente):
    def __init__(self, endereco, cnpj, razao_social):
        super().__init__(endereco)
        self._cnpj = cnpj
        self._razao_social = razao_social
    
    @property
    def cnpj(self):
        return self._cnpj
    
    def __repr__(self):
        return f'{self.__class__.__name__}: {self._cnpj}'

    def __str__(self):
        return f'''
        Razão Social:{self._razao_social}
        CNPJ:{self._cnpj}
        Endereço:{self._endereco}
    '''