# set=conjunto
# set funciona como uma lista desordenada
# nao aceita valores duplicados
# dadoa nao podem ser alterados
# podemos incluir e excluir 

frutas={'maça','banana','morango','tangerina'}
# frutas.add('abacaxi')
# frutas.pop()
# print(frutas, type(frutas))

outras_frutas={'banana','pêra'}
frutas.update(outras_frutas) # atualiza o set com outro set

frutas_citricas={'laranja','limao','tangerina'}
todas_frutas=frutas.union(frutas_citricas) # cria novo set com outros sets

frutas_comum=frutas_citricas.intersection(frutas) # cria set com itens em comum

#print(frutas_comum)

# frozensts
# sao usados dentro de sets, sao imutaveis apos a criação, mantendo o elemento unico do set principal

# grupo_estudante={
#     frozenset({'joao','maria'}),
#     frozenset({'pedro','clara'})
# }

# grupo_estudante.add(frozenset({'marcelo','marcos'}))

# for grupo in grupo_estudante:
#     print(f'grupo: {grupo}')

# operações em conjunto

grupo_a=frozenset({'diego','fernando'})
grupo_b=frozenset({'pedro','fernando'})

uniao=grupo_a|grupo_b # junta dois frozensets
# print(uniao)

intersecao=grupo_a&grupo_b # mostra itens em comum
# print(intersecao)

diferenca=grupo_a-grupo_b # mostra itens diferentes
# print(diferenca)