soma=0
num=0
print(f'digite sair para interromper')
while True:
    num=input('numero: ').lower().strip(' ')
    if num=='sair':
        break
    else:
        soma+=int(num)
print(f'soma = {soma}')

# break: interrompe o loop
# for i in range(5):
#     if i==3:
#         break
#     print(i)

# contine: pra proxima iteração do loop
# for i in range(5):
#     if i==3:
#         continue
#     print(i)

# pass: placeholder
# nao faz nada

# exit(): interrompe o codigo inteiro