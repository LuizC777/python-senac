idade=int(input('digite sua idade: '))
tem_cnh=input('possui cnh?(y/n): ')
if tem_cnh=='y':
    tem_cnh=True
else:
    tem_cnh=False

if idade>=18:
    if tem_cnh:
        print('voce pode dirigir')
    else:
        print('tire habilitacao')
else:
    print('voce e menor de idade')