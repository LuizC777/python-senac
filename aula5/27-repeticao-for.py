# mult=int(input('mult= '))
# for i in range(1,mult+1):
#     print(f'{mult}x{i}={mult*i}')

# for c in range(0,20+1,10):
#     print(c)

# for c in range(20,1-1,-1):
#     print(c)

# soma=0
# for c in range(1,4+1):
#     numero=int(input('digite um numero: '))
#     soma+=numero
# print(soma)

# contador=1
# lista=['luiz','romeo','raissa','alexandre']
# for  item in lista:
#     print(f'{item}->{contador}')
#     contador+=1

# lista=[]
# for c in range(0,2):
#     nome=input('nome: ')
#     lista.append(nome)
# print(lista)

lista_produtos={
    'computador':3000.25,
    'impressora':250.60,
    'teclado':100
}
for produto in lista_produtos:
    print(f'produto:{produto} custa:{lista_produtos[produto]}')