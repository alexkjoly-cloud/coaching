import openpyxl,sys,collections
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
ws=wb[sys.argv[2]]
rows=list(ws.iter_rows(values_only=True))
print('EN-TETE:',rows[0])
data=[r for r in rows[1:] if any(c not in (None,'') for c in r)]
print('lignes non vides:',len(data))
for r in data[:5]: print(r)
