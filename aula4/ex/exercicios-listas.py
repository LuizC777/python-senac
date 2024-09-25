# Exercício 1: Criar e Exibir uma Lista
# Crie uma lista chamada frutas que contenha pelo menos 5 tipos de frutas.
# frutas = "maçã", "banana", "laranja", "uva", "kiwi"
# Exiba a lista de frutas na tela.
# Saida: Lista de frutas: [frutas]
frutas = ["maçã", "banana", "laranja", "uva", "kiwi"]
print(frutas)
#######################################################################

# Exercício 2: Adicionar e Remover Elementos
# Adicione mais uma fruta à lista frutas criada no exercício anterior.
# Remova a primeira fruta da lista.
# Exiba a lista atualizada.
# Saida: Lista de frutas após adições e remoções: [frutas]
frutas.append('abacaxi')
frutas.pop(0)
print(frutas)
#######################################################################

# Exercício 3: Ordenar a Lista
# Crie uma nova lista chamada numeros com os números: 3, 1, 4, 1, 5, 9, 2, 6, 5.
# Ordene a lista numeros em ordem crescente.
# Exiba a lista ordenada.
# Saida: Lista de números ordenada: [numeros]
num=[3, 1, 4, 1, 5, 9, 2, 6, 5]
num.sort()
print(f'lista de numeros ordenados: {num}')
#######################################################################

# Exercício 4: Fatiamento de Listas
# Usando a lista numeros do exercício anterior, exiba os três primeiros números da lista.
# Exiba os números do meio (ou seja, exclua os primeiros e os últimos dois).
# Exibindo os três primeiros números da lista 'numeros'
# Saida 1: Três primeiros números: [3, 1, 4]
# Saida 2: Números do meio: [4, 1, 5, 9, 2]
print(f'tres primeiros numeros: {num[0:3]}')
print(f'numeros do meio: {num[2:7]}')
#######################################################################

# Exercício 5: Encontrar o Maior e Menor Número
# Usando a lista numeros, encontre e exiba o maior e o menor número da lista.
# Encontrando o maior e o menor número na lista 'numeros'
# Saida 1:  Maior número: [maior_numero]
# Saida 2:  Menor número:: [menor_numero]
print(f'maior numero: {max(num)}')
print(f'menor numero: {min(num)}')
#######################################################################

# Exercício 6: Contar Elementos
# Crie uma lista chamada animais com os seguintes elementos: "gato", "cachorro", "pássaro", "gato", "peixe".
# Conte quantas vezes o "gato" aparece na lista e exiba o resultado.
# Saida: O 'gato' aparece [contagem_gato] vezes na lista.
animais=["gato", "cachorro", "pássaro", "gato", "peixe"]
print(f'gato aparece {animais.count('gato')} vezes na lista.')
#######################################################################


# Exercício 10: Remover Duplicatas
# Crie uma lista chamada itens com os seguintes elementos: ["maçã", "banana", "maçã", "laranja", "banana", "uva"].
# Crie uma nova lista que contenha apenas os itens únicos (sem duplicatas) e exiba essa lista.
# Saida: Itens únicos [itens]
frutas2=list(set(["maçã", "banana", "maçã", "laranja", "banana", "uva"]))
#frutas_s=set(frutas2)
#frutas_unicas=list(frutas_s)
frutas2.sort()
print(f'itens unicos: {frutas2}')