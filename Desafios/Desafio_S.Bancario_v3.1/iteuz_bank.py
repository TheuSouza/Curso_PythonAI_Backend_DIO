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
                    # cadastrar cliente pessoa física.
                    gerente.cadastrar_pessoa_fisica(clientes_pessoa_fisica)
                elif opcao == 2:
                    # cadastrar cliente pessoa jurídica.
                    gerente.cadastrar_pessoa_juridica(clientes_pessoa_juridica)
                elif opcao == 3:
                    # Retornar ao menu anterior.
                    sleep(0.5)
                    continue
                else:
                    # Opção invalida.
                    ze.erro()

            elif opcao == 2:
                # cadastrar conta e vincular cliente.
                gerente.cadastrar_conta(contas, clientes_pessoa_fisica, clientes_pessoa_juridica)
            elif opcao == 3:
                # Listar Clientes e contas.
                gerente.listar_clientes(clientes_pessoa_fisica, clientes_pessoa_juridica)
            elif opcao == 4:
                # Relatório de transações.
                gerente.relatorio_trasacoes(contas)
            elif opcao == 5:
                # Retornar ao menu anterior.
                break
            else:
                # Opção invalida.
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
                # extrato
                cliente.extrato(clientes_pessoa_fisica, clientes_pessoa_juridica)
            elif opcao == 4:
                # Retornar ao menu anterior.
                break
            else:
                # Opção invalida.
                ze.erro()

    elif opcao == 3:
        sleep(0.3)
        ze.fim()
        break
    else:
        # Opção invalida.
        ze.erro()