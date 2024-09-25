pessoas = ['luiz','raissa','gabriel','alexandre']

# print(len(pessoas)) # qntd de itens

# print(pessoas[0]) # primeiro item

# print(pessoas[-1]) # ultimo item

# print(pessoas[2:]) # itens a partir de 2

# print(pessoas[:3]) # itens de tras pra frente

# print(pessoas[1:3]) # itens do 1 ate o *2*

# pessoas[3]='icaro' # altera o indice

#####################################################################################

# pessoas.extend(['livia']) # funcao, adiciona arrays no array

# pessoas.append('ana') # adiciona item no array

# pessoas.insert(3, 'joyce') # adiciona item em um indice declarado

# pessoas.pop(2) # exclui o ultimo quando vazio, ou, um indice

# pessoas.remove('alexandre') # exclui item pelo valor

# pessoas.clear() # exclui todos is itens

# print(pessoas.index('raissa')) # exibe o indice do valor (no primeiro registro)

# print(pessoas.count('raissa')) # conta quantas vezes o valor e citado

# pessoas.sort() # funcao .sort() ordena em ordem alfabetica ou crescente

# pessoas2=pessoas.copy() # faz uma copia do array

####################################################################################

num=[33, 25, 60, 10, 20]
num=[1,8,5,4,0,3,2,9,6]

# num.sort()
# num.reverse() # funcao .reverse reverte a ordem

# maior_num=max(num) # imprime o maior
# menor_num=min(num) # imprime o menor
# print(maior_num)
# print(menor_num)
# print(num)

# lista aninhada
turma=[ 
    ['joao',20,'desenvolvedor web'],
    ['maria',22,'python'],
    ['diego',32,'php'],
]
print(turma[1][0])
print(type(turma))