from openpyxl import Workbook
workbook=Workbook()
sheet=workbook.active

dados = [
    ('nome','idade','cidade'),
    ('joao',25,'sao paulo'),
    ('maria',29,'rio de janeiro'),
    ('julieta',18,'belo horizonte')
]


for c in dados:
    sheet.append(c)

sheet.auto_filter.ref='A1:C4'


workbook.save('dados.xlsx')