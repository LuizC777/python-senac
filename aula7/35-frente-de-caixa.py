precos={
    'sanduiches':{
        'Big Mac' : 20.00,
        'Duplo Quarteirão' : 25.00,
        'Big Tasty' : 22.00
    },
    'bebidas':{
        'Coca-Cola' : 5.00,
        'Fanta' : 5.00,
        'Del Valle Laranja' : 6.00
    },
    'batatas':{
        'Pequena' : 7.00,
        'Média' : 9.00,
        'Grande' : 11.00
    }
}
tipo_batata=''
tipo_bebida=''
tipo_sanduiche=''
# Função que recebe o nome do cliente e inicia o pedido

def pegar_nome_cliente(nome):
    print(f'Vamos iniciar o pedido - Cliente: {nome}')

# Função que exibe o sanduiche escolhido

def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduiche: {tipo_sanduiche}')

# Função que exibe a bebida escolhida

def pegar_bebida(tipo_bebida):
    print(f'Você escolheu a bebida: {tipo_bebida}')

# Função que exibe a batata escolhida

def pegar_batata(tipo_batata):
    print(f'Você escolheu a batata do tamanho: {tipo_batata}')

# Função que monta o combo e chama as funções necessárias para exibir as escolhas

def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)

############################################ Funcao de achar o pedido ############################################

def escolher_opcao_sanduiche():
    while True:
        sanduiche = input('Digite o código do sanduíche: \n1 - Big Mac (R$ 20,00) \n2 - Duplo Quarteirão (R$ 25,00) \n3 - Big Tasty (R$ 22,00) \nV - Voltar \nS - Sair\nOpcao: ')
        sanduiche.upper()

        if sanduiche == "S":
            exit()

        opcoes = {'1': 'Big Mac', '2' : 'Duplo Quarteirão', '3': 'Big Tasty', 'v':'' }

        if sanduiche in opcoes:
            return opcoes[sanduiche]
        
        print('Opção inválida, tente novamente')

def escolher_opcao_bebida():
    while True:
        bebida = input('Digite o código da bebida: \n1 - Coca-Cola (R$ 5,00) \n2 - Fanta (R$ 5,00) \n3 - Del Valle Laranja (R$ 6,00) \nV - Voltar \nS - Sair\nOpcao: ')
        bebida.upper()

        if bebida == "S":
            exit()

        opcoes = {'1': 'Coca-Cola', '2' : 'Fanta', '3': 'Del Valle Laranja', 'v':'' }

        if bebida in opcoes:
            return opcoes[bebida]
        
        print('Opção inválida, tente novamente') 

def escolher_opcao_batata():
    while True:
        batata = input('Digite o código da batata: \n1 - Pequena (R$ 7,00) \n2 - Media (R$ 9,00) \n3 - Grande (R$ 11,00) \nV - Voltar \nS - Sair\nOpcao: ')
        batata.upper()

        if batata == "S":
            exit()

        opcoes = {'1': 'Pequena', '2' : 'Media', '3': 'Grande', 'v':'' }

        if batata in opcoes:
            return opcoes[batata]
        
        print('Opção inválida, tente novamente')

def fim():


    print(f'{''.center(10,'*')}\nPedido:\n{nome_cliente}')
    if tipo_sanduiche:
        pegar_sanduiche(tipo_sanduiche)
    if tipo_bebida:
        pegar_bebida(tipo_bebida)
    if tipo_batata:
        pegar_batata(tipo_batata)
    print(f'\n{''.center(10,'*')}')
    

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