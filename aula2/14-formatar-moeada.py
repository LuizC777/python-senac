import locale

#define o locale para o formato do brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor = 10000.00

#formatando o numero como moeda
valor_formatado=locale.currency(valor, grouping=True)

print(valor, valor_formatado)

