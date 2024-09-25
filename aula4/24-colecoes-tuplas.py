# uma tupla (tuple) em python e uma sequencia imutavel de valores de qualquer tipo

# cordenadas=(-49,74,121)
# print(cordenadas)
# print(type(cordenadas))

# cordenadas2=(-30,23,164)
# tupla_concatenada=cordenadas+cordenadas2
# print(tupla_concatenada)

######################################################################################

# tuplas com repetições:
# repeticoes=('python,')*5
# print(repeticoes, 'oi')

# lista=[1,2,3,4]
# lista=tuple(lista) # converte pra tupla

######################################################################################

# pessoa=('luiz',20,'desenvolvedor')
# nome, idade, profissao = pessoa
# print(f'Nome: {nome}\nIdade: {idade}\nProfissão: {profissao}')

tupla_aninhada=(
    ('maçã',1),
    ('banana',2),
    ('laranja',3)
)
fruta1,fruta2,fruta3=tupla_aninhada
print(fruta1[0])