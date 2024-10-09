# abrindo ou criando arquivo 'nome-do-arquivo.txt' no modo de escrita

with open('bibliotecas/txt/exemplo.txt','w', encoding='utf-8') as arquivo:
    # escrevendo no arquivo
    arquivo.write('1 Olá este e o meu primeiro arquivo de texto criado com python\n')
    arquivo.write('2 Essa e a segunda linha')

with open('bibliotecas/txt/exemplo.txt','a', encoding='utf-8') as arquivo:
    arquivo.write('\n3 essa e uma nova linha adicionada ao arquivo')

print('conteudo adicionado com sucesso')

def apagar(count,name):
    with open(name,'r', encoding='utf-8') as arquivo:
        linhas=arquivo.readlines()
        print(linhas)

    with open(name,'w', encoding='utf-8') as arquivo:
        for num, linha in enumerate(linhas):
            if num !=count-1:
                arquivo.write(linha)
apagar(1,'bibliotecas/txt/exemplo.txt')