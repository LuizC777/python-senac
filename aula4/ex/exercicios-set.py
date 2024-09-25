# Exercício 1: Criar um Conjunto
# Criando um conjunto chamado frutas = "maçã", "banana", "laranja"
# Saida Conjunto de frutas: [frutas]
frutas={"maçã", "banana", "laranja"}
print(frutas)
# #############################################

# Exercício 2: Adicionar Elementos ao Conjunto
# Saida: Conjunto de frutas após adição: [frutas]
frutas.add('pera')
print(frutas)

##########################################################

# Exercício 3: Remover Elementos do Conjunto
# Removendo uma fruta do conjunto usando remove
# Saida: Conjunto de frutas após remoção: [frutas]
frutas.remove('banana')
print(frutas)
###############################################################33

# Exercício 4: Verificar a Existência de um Elemento
# Verificando se a fruta 'laranja' está no conjunto
# Use a condicional if e else
# Saida verdadeira A fruta 'laranja' está no conjunto.
# Saida Falsa A fruta 'laranja' está no conjunto.

# frutas=list(frutas)
# if frutas.count('laranja')>0:
#     print(f'A fruta laranja está no conjunto')
# else:
#     print(f'A fruta laranja não está no conjunto')
if 'laranja' in frutas:
    print(f'A fruta laranja está no conjunto')
else:
     print(f'A fruta laranja não está no conjunto')
###########################################

# Exercício 5: Operações de União
# Criando outro conjunto de frutas 
# frutas_citricas = "laranja", "limão", "tangerina"
# Saida: Todas as frutas: [todas_as_frutas]

frutas_citricas = {"laranja", "limão", "tangerina"}
todas_frutas=frutas.union(frutas_citricas)
print(f'Todas as frutas: {todas_frutas}')
###########################################

# Exercício 6: Operações de Interseção
# Criando um conjunto de frutas tropicais
# frutas_tropicais = "maçã", "banana", "coco"
# Encontrando a interseção entre os dois conjuntos usando .intersection 
# Saida Frutas comuns: [frutas_comuns]

frutas_tropicais = {"maçã", "banana", "coco"}
frutas_comuns=frutas.intersection(frutas_tropicais)
print(f'frutas comuns: {frutas_comuns}')
# ########################################################

# Exercício 7: Diferença de Conjuntos
# Crie um conjunto de frutas de inverno
# frutas_inverno = "kiwi", "maçã", "pêra"
# Encontrando a diferença entre 'frutas' e 'frutas_inverno' usando .difference
# Saida Frutas que não estão no inverno: [frutas_diferentes]

frutas_inverno = {"kiwi", "maçã", "pêra"}
frutas_dif=frutas.difference(frutas_inverno)
print(f'frutas que nao estao no inverno: {frutas_dif}')
######################################################################

# Exercício 8: Conjunto de Elementos Únicos
# Crie uma lista com frutas repetidas
# lista_frutas = "maçã", "banana", "laranja", "maçã", "uva", "banana"
# Convertendo a lista em um conjunto para obter elementos únicos, usando o set()
# Saida: Frutas únicas: [frutas_unicas]

lista_frutas = set(["maçã", "banana", "laranja", "maçã", "uva", "banana"])
print(f'frutas unicas: {lista_frutas}')
################################################################

# Exercício 9: Tamanho do Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva"
# Obtendo o tamanho do conjunto de frutas, usando o len()
# Saida: O tamanho do conjunto de frutas é: [tamanho_frutas]
conjunto_frutas= {"maçã", "banana", "laranja", "maçã", "uva"}
print(f'O tamanho do conjunto de frutas é: {len(conjunto_frutas)}')
##############################################################

# Exercício 10: Limpar um Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva" 
# Limpando todos os elementos do conjunto, usando .clear()
# Saida: Conjunto de frutas após limpeza: frutas
conjunto_frutas2= {"maçã", "banana", "laranja", "maçã", "uva" }
conjunto_frutas2.clear()
print(f'Conjunto de frutas após limpeza: {conjunto_frutas2}')