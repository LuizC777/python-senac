# Exercício 1:
# Solicite ao usuário que insira seu nome e idade. Em seguida, exiba uma mensagem de boas-vindas.
# mensagem Olá, [nome]! Você tem [idade] anos.
nome=input('digite seu nome: ')
idade=int(input('digite sua idade: '))

print(f'Bem vindo {nome}!, você tem {idade} anos.')

################################################################

# Exercício 2:
# Solicite ao usuário que insira um numero flutuante
# soma com o valor constante 25
# mensagem = A soma de [numero] mais [NUMERO_CONSTANTE] é [resultado].

# Lembrete: Temos que converter o numero para flutuante
num=float(input('digite um numero: '))
VALOR=25
resultado=num+VALOR
print(f'a soma de {num} com {VALOR} e igual a {resultado}')

#################################################################

# Exercício 3:
# Crie uma variável chamada nome_completo para armazenar o nome completo de uma pessoa.
# Crie outra variável chamada idade para armazenar a idade da pessoa.
# Crie uma variável salario_mensal para armazenar o salário mensal da pessoa.
# Por fim, exiba essas informações de forma concatenada no seguinte formato:
# "Meu nome é [nome_completo], tenho [idade] anos e ganho R$ [salario_mensal] por mês."

##* Extra Formatar o salario_mensal como moeda
import locale
locale.setlocale(locale.LC_ALL, 'pt-br.UTF-8')
nome_completo='luiz claro'
idade=20
salario_mensal=2000
sal_for=locale.currency(salario_mensal, grouping=True)
        #f'{numero:,.2f}'.replace('.','x').replace(',','.').replace('x',',')
print(f'Meu nome e {nome_completo}, tenho {idade} anos e ganho {sal_for} por mes.')
#################################################################

# Exercício 4:
# Solicite ao usuário dois números inteiros e exiba a soma dos números.
num1=int(input('digite o numero 1: '))
num2=int(input('digite o numero 2: '))
res=num1+num2
print(f'{num1}+{num2}={res}')

#################################################################

#Exercício 5:
# Peça ao usuário que insira um número decimal (float) e exiba o dobro desse número.
# Saida = O dobro de ? é ?.
# exemplo = entrada 5 então a saida seria "O dobro de 5 é 10"
num1=float(input('insira um numero: '))
print(f'o dobro de {num1} e {num1*2}')
#################################################################

# Exercício 6:

# Peça ao usuário que insira seu nome e se está estudando atualmente (responda com "sim" ou "não"). Exiba uma mensagem confirmando sua resposta.
# entrada = Digite seu nome
# entrada = Está estudando atualmente, digite "sim" ou "não 
## temos que tratar o valor de entrada "sim" ou "não com .strip().lower()
# saida =[nome], você está estudando: [esta_estudando].")
# a variavel [esta_estudando] vai ser igual a true ou false
######
## Extra implementar if else
## se a variavel [esta_estudando] = True 
## saida = [nome], ótimo continue assim!
## se não 
## saida = [nome], vamos estudar!
nome=input('digite seu nome: ')
status=''
while status!=True and status!=False:
    status=input('esta estudadando?(s/n): ').lower().strip(' ')
    if status=='s':
        status=True
        print(f'{nome},\notimo! continue assim')
    elif status=='n':
        status=False
        print(f'{nome},\nvamos estudar!')
#################################################################

# Exercício 7:
# Peça ao usuário para inserir seu nome e um número, depois exiba o nome repetido esse número de vezes.

#################################################################

# Exercício 8:
# Solicite ao usuário que insira seu peso e altura, calcule seu IMC (Índice de Massa Corporal) e exiba o resultado.
# Fórmula do IMC: IMC = peso / altura²

#################################################################

# Exercício 9:
# Solicite ao usuário que insira a quantidade de horas trabalhadas e o valor da hora. Calcule e exiba o salário bruto.

#################################################################

# Exercício 10:
# Solicite ao usuário um valor de produto e uma porcentagem de desconto. Calcule e exiba o valor final com o desconto aplicado.

#################################################################

#Exercício 11:
# Escreva um programa que solicite ao usuário um número e verifique se o número é positivo ou negativo. Se o número for zero, informe que é zero.

# numero > 0: "O número é positivo."
# numero < 0: "O número é negativo."
# numero == 0: "O número é zero."

#################################################################

# Exercício 12:
# Peça ao usuário para inserir um número inteiro e verifique se é par ou ímpar. Exiba o resultado.

#################################################################

# Exercício 13:
# O programa recebe o valor de compra e se o cliente for um cliente frequente (responda com "sim" ou "não")
# O cliente recebe desconto se suas compras forem maiores que 1000 'ou' se for cliente frequente
## temos que tratar o valor de entrada "sim" ou "não" com .strip().lower()
# utilize a conditional if e else

#################################################################


# Exercício 14:
# Crie um programa que solicite ao usuário 3 notas de um aluno (entre 0 e 10), calcule a média e exiba a classificação da nota com base na média final:

# Média menor que 5: "Reprovado"
# Média entre 5 e 6: "Recuperação"
# Média maior ou igual a 7: "Aprovado"

#################################################################

# Exercício 15:
# Escreva um programa que solicita a temperatura em graus Celsius e exibe se o clima está frio, agradável ou quente.

# Menor que 15: "O clima está frio"
# Entre 15 e 25: "O clima está agradável"
# 26 ou mais: "O clima está quente."

#################################################################

# Exercício 16:
# Crie um programa que solicite ao usuário que insira sua idade e exiba uma mensagem com base na faixa etária da pessoa:

# Menor de 12 anos: "Você é uma criança."
# Entre 12 e 17 anos: "Você é um adolescente."
# Entre 18 e 59 anos: "Você é um adulto."
# 60 anos ou mais: "Você é idoso."




