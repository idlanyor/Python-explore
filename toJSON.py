import pandas as pd

namafile = input("File XLSX :")

df = pd.read_excel(namafile)

dataJson = df.to_json(orient='records')

