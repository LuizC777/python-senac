# Dicionario com os preços dos produtos

precos = {
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

# Função que recebe o nome do cliente e inicia o pedido

def pegar_nome_cliente(nome):
    print(f'Vamos iniciar o pedido - Cliente: {nome}')

# pegar_nome_cliente('Fulano')

# Função que exibe o sanduiche escolhido
def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduiche: {tipo_sanduiche}')

# pegar_sanduiche('Duplo Quarteirão')

# Função que exibe a bebida escolhida

def pegar_bebida(tipo_bebida):
    print(f'Você escolheu a bebida: {tipo_bebida}')

# pegar_bebida('Coca-Cola')


# Função que exibe a batata escolhida

def pegar_batata(tipo_batata):
    print(f'Você escolheu a batata do tamanho: {tipo_batata}')

# pegar_batata('Pequena')


# Função que monta o combo e chama as funções necessárias para exibir as escolhas
def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)

# montar_combo('Diego','Big Tasty','Coca-cola','Pequena')


# Função para escolher o tipo de sanduíche
def escolher_opcao_sanduiche():
    while True:
        sanduiche = input('Digite o código do sanduíche: \n1 - Big Mac (R$ 20,00) \n2 - Duplo Quarteirão (R$ 25,00) \n3 - Big Tasty (R$ 22,00) \nV - Voltar \nS - Sair')

        if sanduiche.upper() == "V":
            return "voltar"
        elif sanduiche.upper == "S":
            exit()

        opcoes = {'1': 'Big Mac', '2' : 'Duplo Quarteirão', '3': 'Big Tasty' }

        if sanduiche in opcoes:
            return opcoes[sanduiche]
        
        print('Opção inválida, tente novamente') #### Terminamos aqui

def escolher_opcao_bebida():
    while True:
        bebida = input('Digite o código da bebida: \n1 - Coca-Cola (R$ 5,00) \n2 - Fanta (R$ 5,00) \n3 - Del ValleLaranja (R$ 6,00) \nV - Voltar \nS - Sair')

        if bebida.upper() == "V":
            return "voltar"
        elif bebida.upper == "S":
            exit()

        opcoes = {'1': 'Coca-Cola', '2' : 'Fanta', '3': 'Del Valle Laranja' }

        if bebida in opcoes:
            return opcoes[bebida]
        
        print('Opção inválida, tente novamente') #### Terminamos aqui

def escolher_opcao_batata():
    while True:
        batata = input('Digite o código da batata: \n1 - Pequena (R$ 7,00) \n2 - Média (R$ 9,00) \n3 - Grande (R$ 11,00) \nV - Voltar \nS - Sair')

        if batata.upper() == "V":
            return "voltar"
        elif batata.upper == "S":
            exit()

        opcoes = {'1': 'Pequena', '2' : 'Média', '3': 'Grande' }

        if batata in opcoes:
            return opcoes[batata]
        
        print('Opção inválida, tente novamente') #### Terminamos aqui

############################################## loop do pedido ##############################################


while True:
    pedidos_todos=[]
    nome_cliente = input('Digite o nome do cliente (ou [s] para sair): ')
    if nome_cliente.upper() == 'S':
        exit()

    pegar_nome_cliente(nome_cliente)

    while True:
        pedido = input('Digite o código do tipo e pedido: \n1 - Somente sanduíche \n2 - Somente bebida \n3 - Somente batata \n4 - Combo \nF - Fechar caixa \nV - Voltar \nS - Sair \n********************* \n' )

        if pedido.upper() == "S":
            exit()
        elif pedido == "V":
            break

        # Dicionario para armazenar os itens do pedido

        pedido_cliente={
            'sanduiche': None,
            'bebida' : None,
            'batata' : None
        }

        # Seletor do menu

        if pedido == '1':
            tipo_sanduiche = escolher_opcao_sanduiche() # Escolhe o sanduíche
            if tipo_sanduiche=='voltar':
                continue
            pegar_sanduiche(tipo_sanduiche)
            pedido_cliente['sanduiche']=tipo_sanduiche


        if pedido == '2':
            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida=='voltar':
                continue
            pegar_bebida(tipo_bebida)
            pedido_cliente['bebida']=tipo_bebida


        if pedido == '3':
            tipo_batata = escolher_opcao_batata()
            if tipo_batata=='voltar':
                continue
            pegar_batata(tipo_batata)
            pedido_cliente['batata']=tipo_batata

        elif pedido == '4':

            tipo_sanduiche = escolher_opcao_sanduiche() # Escolhe o sanduíche
            if tipo_sanduiche=='voltar':
                continue
            pegar_sanduiche(tipo_sanduiche)
            pedido_cliente['sanduiche']=tipo_sanduiche

            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida=='voltar':
                continue
            pegar_bebida(tipo_bebida)
            pedido_cliente['bebida']=tipo_bebida

            tipo_batata = escolher_opcao_batata()
            if tipo_batata=='voltar':
                continue
            pegar_batata(tipo_batata)
            pedido_cliente['batata']=tipo_batata

        elif pedido.upper() == 'F':

            print(f'Fechando o caixa'.center(80,'*'))
            print(f'Cliente: {nome_cliente}')
            total=0

            for index, pedido in enumerate(pedidos_todos,1):
                print(f'\nPedido {index}')
                if pedido['sanduiche']:
                    print(f'sanduiche: {pedido['sanduiche']} R$ {precos['sanduiches'][pedido['sanduiche']]:.2f}')
                    total+=precos['sanduiches'][pedido['sanduiche']]

                if pedido['bebida']:
                    print(f'bebida: {pedido['bebida']} R$ {precos['bebidas'][pedido['bebida']]:.2f}')
                    total+=precos['bebidas'][pedido['bebida']]

                if pedido['batata']:
                    print(f'batata: {pedido['batata']} R$ {precos['batatas'][pedido['batata']]:.2f}')
                    total+=precos['batatas'][pedido['batata']]

            print(f'\nTotal do pedido: R$ {total:.2f}')
            pedidos_todos=[]
            print('Caixa Fechado'.center(80,'*'))


        else:
            print('Opcao invalida')
        pedidos_todos.append(pedido_cliente)