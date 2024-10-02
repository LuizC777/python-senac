iniciar=input('iniciar?(s/n): ').lower().strip(' ')
nomes=[]
while iniciar=='s':
    nome=input('digite o nome(\'s\' para sair): ')
    nomes.append(nome)
    if nome=='s':
        nomes.pop()
        print (nomes)
        break