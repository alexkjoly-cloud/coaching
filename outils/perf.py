import openpyxl,sys,collections
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
ws=wb[sys.argv[2]]
rows=list(ws.iter_rows(values_only=True))[1:]
perf=collections.defaultdict(dict)   # (seance,exo) -> {sem: [(serie,kg,reps,rir)]}
bil=collections.defaultdict(dict)
notes=[]
for r in rows:
    if not r or not r[10]: continue
    sem,sea,exo,ser,kg,reps,rir,fait,note,maj,cle=r
    c=str(cle)
    if c.startswith('perf|'):
        perf[(sea,exo)].setdefault(sem,[]).append((ser,kg,reps,rir))
    elif c.startswith('bilan|'):
        bil[sem][exo]=kg if kg is not None else note
    elif c.startswith('note|'):
        if note: notes.append((sem,sea,str(note)))
def k(s):
    try: return int(str(s).replace('S',''))
    except: return 99
print('===== PERFS =====')
for (sea,exo),d in sorted(perf.items()):
    print(f'\n--- {sea} · {exo}')
    for sem in sorted(d,key=k):
        ss=sorted(d[sem],key=lambda x:str(x[0]))
        txt=' | '.join(f'{kg}kg×{reps}' + (f' RIR{rir}' if rir not in (None,'') else '') for _,kg,reps,rir in ss)
        print(f'   {sem}: {txt}')
print('\n===== BILANS =====')
for sem in sorted(bil,key=k):
    print(f'\n{sem}:')
    for f,v in bil[sem].items(): print(f'   {f}: {v}')
print('\n===== NOTES DE SEANCE =====')
for sem,sea,n in sorted(notes,key=lambda x:(k(x[0]),str(x[1]))):
    print(f'\n[{sem} · {sea}] {n}')
