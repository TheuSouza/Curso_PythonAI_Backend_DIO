from time import sleep
import zestilo as ze
import funcao_gerente as gerente

ze.bem_vindo()
while True:
    opcao = ze.menu0()

    if opcao == 1:

        while True:
            opcao = ze.menu2()
            if opcao == 1:
                opcao = ze.menu3()
                if opcao == 1:
                    gerente.cadastrar_pessoa_fisica()
                    # cadastrar cliente pessoa física.
                elif opcao == 2:
                    gerente.cadastrar_pessoa_juridica()
                    # cadastrar cliente pessoa jurídica.
                elif opcao == 3:
                    sleep(0.5)
                    continue
                else:
                    ze.erro()
            elif opcao == 2:
                gerente.cadastrar_conta()
                # cadastrar conta
            elif opcao == 3:
                gerente.listar_clientes()
                # Listar Clientes
            elif opcao == 4:
                break
            else:
                ze.erro()

    elif opcao == 2:

        while True:
            opcao = ze.menu1()
            if opcao == 1:
                pass
                # depositar
            elif opcao == 2:
                pass
                # sacar
            elif opcao == 3:
                pass
                # extrato
            elif opcao == 4:
                break
            else:
                ze.erro()

    elif opcao == 3:
        break
    else:
        ze.erro()