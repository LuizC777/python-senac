# Função que recebe o nome do cliente e inicia o pedido

def pegar_nome_cliente(nome):
    print(f'Vamos iniciar o pedido - Cliente: {nome}')

# Função que exibe o sanduiche escolhido

def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduiche: {tipo_sanduiche[0]} R$ {str(tipo_sanduiche[1]).replace('.',',')}')

# Função que exibe a bebida escolhida

def pegar_bebida(tipo_bebida):
    print(f'Você escolheu a bebida: {tipo_bebida[0]} R$ {str(tipo_bebida[1]).replace('.',',')}')

# Função que exibe a batata escolhida
batata=''
def pegar_batata(tipo_batata):
    print(f'Você escolheu a batata do tamanho: {tipo_batata[0]} R$ {str(tipo_batata[1]).replace('.',',')}')

# Função que monta o combo e chama as funções necessárias para exibir as escolhas

def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)


############################################ Funcao de achar o pedido ############################################


def escolher_opcao_sanduiche():
    sanduiche_custo=0
    while True:
        sanduiche = input('Digite o código do sanduíche: \n1 - Big Mac (R$ 20,00) \n2 - Duplo Quarteirão (R$ 25,00) \n3 - Big Tasty (R$ 22,00) \nV - Voltar \nS - Sair\nOpcao: ')
        sanduiche=sanduiche.upper()

        if sanduiche == "S":
            exit()
        if sanduiche =='V':
            sanduiche=4
        sanduiche=int(sanduiche)

        opcoes = {1: 'Big Mac', 2 : 'Duplo Quarteirão', 3: 'Big Tasty', 4:0 }
        preco_sanduiche = {1: 20.0, 2 : 25.0, 3: 22.0, 4:0}

        if sanduiche in preco_sanduiche:
            sanduiche_custo=preco_sanduiche[sanduiche]
        if sanduiche in opcoes:
            return opcoes[sanduiche],sanduiche_custo
        
        print('Opção inválida, tente novamente')


def escolher_opcao_bebida():
    bebida_custo=0
    while True:
        bebida = input('Digite o código da bebida: \n1 - Coca-Cola (R$ 5,00) \n2 - Fanta (R$ 5,00) \n3 - Del Valle Laranja (R$ 6,00) \nV - Voltar \nS - Sair\nOpcao: ')
        bebida=bebida.upper()

        if bebida == "S":
            exit()
        if bebida == 'V':
            bebida=4
        bebida=int(bebida)
        
        opcoes = {1: 'Coca-Cola', 2 : 'Fanta', 3: 'Del Valle Laranja', 4:0 }
        preco_bebida = {1: 5.0, 2 : 5.0, 3: 6.0, 4:0}

        if bebida in preco_bebida:
            bebida_custo=preco_bebida[bebida]
        if bebida in opcoes:
            return opcoes[bebida],bebida_custo
        
        print('Opção inválida, tente novamente') 


def escolher_opcao_batata():
    batata_custo=0
    while True:
        batata = input('Digite o código da batata: \n1 - Pequena (R$ 7,00) \n2 - Media (R$ 9,00) \n3 - Grande (R$ 11,00) \nv - Voltar \nS - Sair\nOpcao: ')
        batata=batata.upper()

        if batata == "S":
            exit()
        if batata == 'V':
            batata=4
        batata=int(batata)

        opcoes = {1: 'Pequena', 2 : 'Media', 3: 'Grande', 4:0 }
        preco_batata = {1 : 7.0, 2 : 9.0, 3 : 11.0, 4:0 }

        if batata in preco_batata:
            batata_custo=preco_batata[batata]
        if batata in opcoes:
            print(batata_custo)
            return opcoes[batata],batata_custo
        print('Opção inválida, tente novamente')


def fim():

    print(f'{''.center(10,'*')}\n{nome_cliente}\nPedido:')
    if tipo_sanduiche!=(0,0):
        pegar_sanduiche(tipo_sanduiche)
    if tipo_bebida!=(0,0):
        pegar_bebida(tipo_bebida)
    if tipo_batata!=(0,0):
        pegar_batata(tipo_batata)
    print(f'Total: R$ {str((tipo_batata[1])+(tipo_bebida[1])+(tipo_sanduiche[1])).replace('.',',')}')
    print(f'\n{''.center(10,'*')}')
    

tipo_batata=(0,0)
tipo_bebida=(0,0)
tipo_sanduiche=(0,0)

############################################ inicio do pedido ############################################


while True:
    nome_cliente = input('Digite o nome do cliente (ou [s] para sair): ')

    if nome_cliente.upper() == 'S':
        exit()

    pegar_nome_cliente(nome_cliente)

    while True:
        pedido = input('Digite o código do tipo e pedido: \n1 - Somente sanduíche \n2 - Somente bebida \n3 - Somente batata \n4 - Combo \nF - Fechar pedido \nV - Voltar \nS - Sair \n********************* \n' )

        if pedido.upper() == "S":
            exit()
        elif pedido.upper() == "V":
            break
        elif pedido.upper() == 'F':
            fim() 
            tipo_batata=''
            tipo_bebida=''
            tipo_sanduiche=''
            break

        # Dicionario para armazenar os itens do pedido

        if pedido == '1':
            tipo_sanduiche = escolher_opcao_sanduiche() 
        elif pedido == '2':
            tipo_bebida = escolher_opcao_bebida() 
        elif pedido == '3':
            tipo_batata = escolher_opcao_batata()
        elif pedido == '4':
            tipo_sanduiche = escolher_opcao_sanduiche() 
            tipo_bebida = escolher_opcao_bebida() 
            tipo_batata = escolher_opcao_batata()
            fim()
            break
        else:
            print('opcao invalida')