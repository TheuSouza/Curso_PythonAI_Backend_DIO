import cliente
import zcores as zc

def listar_clientes():
    print('Listando clientes...')

def cadastrar_pessoa_fisica(clientes):
    cpf = input(f'{zc.rwhite()}Digite CPF:{zc.reset()}\n=> ').strip()
    busca = [cliente for cliente in clientes if cliente.cpf == cpf]
    if busca:
        print(f'\n{zc.red()}CPF já foi cadastrado!{zc.reset()}')
    else:
        nome = input(f'{zc.rwhite()}Digite Nome completo:{zc.reset()}\n=> ').strip()
        data_nascimento = input(f'{zc.rwhite()}Digite Data de nascimento [DD/MM/AAAA]:{zc.reset()}\n=> ').strip()
        endereco = input(f'{zc.rwhite()}Digite Endereço [Rua, Número, Bairro, Cidade - Estado]:{zc.reset()}\n=> ').strip()

        novo_cliente = cliente.PessoaFisica(cpf=cpf, nome=nome, 
            data_nascimento=data_nascimento, endereco=endereco
            )
        
        clientes.append(novo_cliente)
        print(f'\n{zc.green()}Cliente cadastrado com sucesso!{zc.reset()}')


def cadastrar_pessoa_juridica(clientes):
    cnpj = input(f'{zc.rwhite()}Digite CNPJ:{zc.reset()}\n=> ').strip()
    busca = [cliente for cliente in clientes if cliente.cnpj == cnpj]
    if busca:
        print(f'\n{zc.red()}CNPJ já foi cadastrado!{zc.reset()}')
    else:
        razao_social = input(f'{zc.rwhite()}Digite Razão Social:{zc.reset()}\n=> ').strip()
        endereco = input(f'{zc.rwhite()}Digite Endereço [Rua, Número, Bairro, Cidade - Estado]:{zc.reset()}\n=> ').strip()

        novo_cliente = cliente.PessoaJuridica(
            cnpj=cnpj, razao_social=razao_social, endereco=endereco
            )
        
        clientes.append(novo_cliente)
        print(f'\n{zc.green()}Cliente cadastrado com sucesso!{zc.reset()}')

def cadastrar_conta():
    print('Cadastrando conta...')