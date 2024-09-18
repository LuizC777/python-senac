numero=float(input('digite um valor em moeda: '))
print(numero)

numero_formatado=f'{numero:,.2f}'.replace('.','x').replace(',','.').replace('x',',')
print(f'R$ {numero_formatado}')