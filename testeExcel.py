import pandas as pd
import xlsxwriter

meses = "JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ".split()
arquivo1 = 'req_v4.xlsx' # 1° arquivo
arquivo2 = 'rq_v4.xlsx' # 2° arquivo
coluna_adicionar = []
# Coletar a coluna do 1° arquivo
for i in range(0, len(meses)):
    coluna_adicionar.append(pd.read_excel(arquivo1, sheet_name =meses[i], usecols=[0,1,2,3]))
# Coletar os dados da Página_2 do 2° arquivo para fazer a concatenação/união
df_somar_coluna = pd.read_excel(arquivo2, sheet_name = 'JAN')

df = pd.concat([df_somar_coluna,coluna_adicionar], axis = 1)

from openpyxl import load_workbook

# o livro criado será referente ao 2° arquivo pois ele é quem será editado
book = load_workbook(arquivo2)
writer = pd.ExcelWriter(arquivo2, engine = 'xlsxwriter')
writer.book = book

writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df.to_excel(writer, sheet_name='JAN')

writer.save()
writer.close()