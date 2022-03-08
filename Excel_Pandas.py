import pandas as pd
from pathlib import Path
from datetime import datetime
import os
from openpyxl import load_workbook

def modificar_banco():
    data = datetime.today().strftime('%d/%m/%Y')

    meses = "JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ".split()
    sem = []

    caminho = Path(r"req_v4.xlsx")

    if os.path.isfile(caminho) and os.access(caminho, os.R_OK):
        print("Foi possivel acessar o arquivo, utilizando dados arquivo PC")
    else:
        print("Não foi possivel acessar o arquivo, utilizando arquivo próprio")

    for i in range(0, len(meses)):
        sem.append(pd.read_excel(caminho, sheet_name=meses[i],usecols=[1,2,3,4]))

    df = pd.DataFrame(sem[3])
    tst = len(df.index)
    coluna = tst + 2

    localA = 'A'+f'{coluna}'
    local = 'B'+f'{coluna}'
    local1 = 'C'+f'{coluna}'
    local2 = 'D'+f'{coluna}'
    local3 = 'E'+f'{coluna}'
    wb = load_workbook(caminho)

    ws6 = wb["ABR"]
    ws6[localA].value = tst
    ws6[local].value = data
    ws6[local1].value = 'ifjeifje'
    ws6[local2].value = 32
    ws6[local3].value = 'cnc2'

    print(df)
    print(coluna)
    print(tst)

# Salva arquivo (Se não colocar o caminho complete, ele salva
    wb.save('req_v4.xlsx')

