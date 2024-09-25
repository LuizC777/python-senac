mes={
    'jan':'janeiro',
    'fev':'fevereiro',
    'mar':'março',
    'abr':'abril',
    'mai':'maio',
    'jun':'junho',
    'jul':7,
    1:'ola'
}
mes['jul']='julho' # altera itens
mes['ago']='agosto' # adiciona itens
mes.pop(1) # remove itens
# print(mes)

#####################################################
# Dicionario aninhado

frutas={
    'fruta_1':{
        'nome':'maçã',
        'preco':5.00
    },
    'fruta_2':{
        'nome':'pêra',
        'preco':5.60
    }
}
# print(frutas['fruta_2']['preco'])

chaves=['nome','idade','curso']
val=['maria','23','python']
pessoas=dict(zip(chaves,val))
print(pessoas)