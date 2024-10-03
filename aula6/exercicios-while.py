# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.
count=1
while count<=10:
    print(count)
    count+=1
#########################################################################

# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.
count=0
soma=0
while count<=100:
    soma+=count
    print(soma)
    count+=1
#########################################################################

# Exercício 3: Tabuada do 5
# Imprima a tabuada do 5.
num=1
while num<=10:
    print(num*5)
    num+=1
#########################################################################

# Exercício 4: Números Pares
# Imprima todos os números pares de 1 a 20.
num=1
while num<=20:
    if num%2==0:
        print(num)
    num+=1
#########################################################################

# Exercício 5: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.
num=1
while num<=10:
    print(num*num)
    num+=1
#########################################################################

# Exercício 6: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.
num=10
while num>0:
    print(num)
    num-=1
#########################################################################

# Exercício 7: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.
count=1
soma=1
while count<=5:
    soma*=count
    count+=1
print(soma)
#########################################################################

# Exercício 8: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.
num=1
while num<=20:
    if num%2!=0:
        print(num)
    num+=1
#########################################################################

# Exercício 9: Contar Vogais
# Conte e imprima o número de vogais em uma string.
# string = "Hello, World!"
# vogais = "aeiouAEIOU"
string = "Hello, World!"
vogais = "aeiouAEIOU"
def vog_count(string):
    count=0
    soma=0
    lett=[]
    vogais=[]
    lett.extend((string).lower().strip(' '))
    while count<len(string):
        if lett[count]=='a' or lett[count]=='e' or lett[count]=='i' or lett[count]=='o' or lett[count]=='u':
            vogais.append(lett[count])
            soma+=1
        count+=1
    # vogais=list(set(vogais)) # Tira duplicatas
    # vogais.sort()
    print(f'Vogais={vogais}\nQtd={soma}')
vog_count(vogais)
#########################################################################

# Exercício 10: Gerenciador de Lista de Compras
# Peça ao usuário para adicionar itens à sua lista de compras até que ele digite "sair".
# Inicializa a lista de compras vazia 
# Loop para adicionar itens
# Exibe a lista de compras com o loop FOR

compras=[]
status=0
print(''.center(30,'*'))
print('Digite sua lista de compras\n"sair" para finalizar')
while status!='sair':
    status=input('Item: ')
    compras.append(status)
compras.remove('sair')
print(''.center(30,'*'))
print(f'Lista de compras:')
for item in compras:
    print(item)