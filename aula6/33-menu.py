def menu_principal():
    print(f'Menu principal\nDigite o código do menu:')
    print(f'1: Opção 1')
    print(f'2: Opção 2')
    print(f'3: Opção 3')
    print(f'4: Finalizar')
    print(f'5: Sair')
    print(''.center(20,'*'))

def sub_menu(opcao):
        print(f'Voce está na {opcao}')
        print('1: fazer algo na opção')
        print('2: voltar')
        print('3: sair')
        print(''.center(20,'*'))

def menu():
    while True:

        menu_principal()
        opcao=input('Escolha uma opção: ')

        if opcao=='1':
            sub_menu('Opção 1')
            sub_opcao=input('Escolha uma ação: ')

            if sub_opcao=='1':
                print('Você fez algo na opção 1')
            elif sub_opcao=='2':
                continue
            elif sub_opcao=='3':
                print('Fim'.center(9,'*'))
                exit()
            else:
                print('Opção inválida')

        elif opcao=='2':
            sub_menu('Opção 2')
            sub_opcao=input('Escolha uma ação: ')

            if sub_opcao=='1':
                print('Você fez algo na opção 1')
            elif sub_opcao=='2':
                continue
            elif sub_opcao=='3':
                print('Fim'.center(9,'*'))
                exit()
            else:
                print('Opção inválida')

        elif opcao=='3':
            sub_menu('Opção 3')
            sub_opcao=input('Escolha uma ação: ')

            if sub_opcao=='1':
                print('Você fez algo na opção 1')
            elif sub_opcao=='2':
                continue
            elif sub_opcao=='3':
                print('Fim'.center(9,'*'))
                exit()
            else:
                print('Opção inválida')

        elif opcao=='4':
            print('Finalizar'.center(15,'*'))
            break

        elif opcao=='5':
            print('Sair'.center(15,'*'))
            exit()

        else:
            print('Opção inválida')

menu()