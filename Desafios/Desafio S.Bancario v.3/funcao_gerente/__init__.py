import cliente
import conta as cd
import zcores as zc

def listar_clientes(pessoa_fisica, pessoa_juridica):
    for cliente in pessoa_fisica:
        print()
        print(cliente.__str__())
        for conta in cliente._contas:
            print(conta.__str__())
        print()
    for cliente in pessoa_juridica:
        print()
        print(cliente.__str__())
        for conta in cliente._contas:
            print(conta.__str__())
        print()

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

def cadastrar_conta(contas, pessoa_fisica, pessoa_juridica):
    numero_conta = len(contas) + 1
    tipo_conta =  int(input('''
        Digite qual tipo de conta:
            [1] Conta corrente
            [2] Conta poupança
            
        => '''))
    
    if tipo_conta == 1:
        conta_completa = cd.ContaCorrente(numero_conta)
    elif tipo_conta == 2:
        conta_completa = cd.ContaPoupanca(numero_conta)
    else:
        print(f'\n{zc.red()}Tipo de conta inválido!{zc.reset()}')
       
    filtro_pessoa = int(input('''
        Vincular conta a uma:
            [1] Pessoa física
            [2] Pessoa jurídica
        => '''))

    if filtro_pessoa == 1:
        cpf = input(f'{zc.rwhite()}Digite CPF:{zc.reset()}\n=> ').strip()
        nao_encontrado = True
        for cliente in pessoa_fisica:
            if cliente.cpf == cpf:
                cliente._contas.append(conta_completa)
                print(f'{zc.green()}Conta vinculada com sucesso!{zc.reset()}')
                contas.append(conta_completa)
                nao_encontrado = False
                break
        if nao_encontrado:
            print(f'\n{zc.red()}CPF não encontrado, é necessario fazer o cadastro!{zc.reset()}\n')
            cadastrar_pessoa_fisica(pessoa_fisica)
            for cliente in pessoa_fisica:
                if cliente.cpf == cpf:
                    cliente._contas.append(conta_completa)
                    print(f'{zc.green()}Conta vinculada com sucesso!{zc.reset()}')
                    contas.append(conta_completa)
                    break
                


    elif filtro_pessoa == 2:
        cnpj = input(f'{zc.rwhite()}Digite CNPJ:{zc.reset()}\n=> ').strip()
        nao_encontrado = True
        for cliente in pessoa_juridica:
            if cliente.cnpj == cnpj:
                cliente._contas.append(conta_completa)
                print(f'{zc.green()}Conta vinculada com sucesso!{zc.reset()}')
                contas.append(conta_completa)
                nao_encontrado = False
                break
        if nao_encontrado:
            print(f'\n{zc.red()}CNPJ não encontrado, é necessario fazer o cadastro!{zc.reset()}\n')
            cadastrar_pessoa_juridica(pessoa_juridica)
            for cliente in pessoa_juridica:
                if cliente.cnpj == cnpj:
                    cliente._contas.append(conta_completa)
                    print(f'{zc.green()}Conta vinculada com sucesso!{zc.reset()}')
                    contas.append(conta_completa)
                    break

    else:
        print(f'\n{zc.red()}Opção inválida!{zc.reset()}')
