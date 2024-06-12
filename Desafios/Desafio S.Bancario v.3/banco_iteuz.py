from time import sleep
import zestilo as ze
import funcao_gerente as gerente
import funcao_cliente as cliente

clientes_pessoa_fisica = list()
clientes_pessoa_juridica = list()
contas = list()

ze.bem_vindo()
while True:
    opcao = ze.menu0()

    if opcao == 1:

        while True:
            opcao = ze.menu2()
            if opcao == 1:
                opcao = ze.menu3()
                if opcao == 1:
                    gerente.cadastrar_pessoa_fisica(clientes_pessoa_fisica)
                    # cadastrar cliente pessoa física.
                elif opcao == 2:
                    gerente.cadastrar_pessoa_juridica(clientes_pessoa_juridica)
                    # cadastrar cliente pessoa jurídica.
                elif opcao == 3:
                    sleep(0.5)
                    continue
                else:
                    ze.erro()
            elif opcao == 2:
                gerente.cadastrar_conta(contas, clientes_pessoa_fisica, clientes_pessoa_juridica)
                # cadastrar conta e vincular cliente.
            elif opcao == 3:
                gerente.listar_clientes(clientes_pessoa_fisica, clientes_pessoa_juridica)
                # Listar Clientes e contas.
            elif opcao == 4:
                break
            else:
                ze.erro()

    elif opcao == 2:

        while True:
            opcao = ze.menu1()
            if opcao == 1:
                # depositar
                cliente.deposito(clientes_pessoa_fisica, clientes_pessoa_juridica)
            elif opcao == 2:
                 # sacar
                cliente.saque(clientes_pessoa_fisica, clientes_pessoa_juridica)
            elif opcao == 3:
                pass
                # extrato
            elif opcao == 4:
                break
            else:
                ze.erro()

    elif opcao == 3:
        sleep(0.3)
        print('Encerrando o programa...')
    else:
        ze.erro()