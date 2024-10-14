from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference

workbook=Workbook()

sheet=workbook.active

dados=[
    ('produto','vendas'),
    ('produto A',50),
    ('produto B',30),
    ('produto C',40)
]

for c in dados:
    sheet.append(c)

chart=BarChart()
dados=Reference(sheet,min_col=2,min_row=2,max_col=2,max_row=4)
categorias=Reference(sheet,min_col=1,min_row=2,max_row=4)

chart.add_data(dados, titles_from_data=True)

chart.set_categories(categorias)

sheet.add_chart(chart,'E5')

workbook.save('planilha-grafico.xlsx')