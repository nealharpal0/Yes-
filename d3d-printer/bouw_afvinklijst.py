import csv,json,sys,pathlib
d=pathlib.Path(__file__).parent
rows=list(csv.DictReader(open(d/'onderdelenlijst.csv',encoding='utf-8'),delimiter=';'))
items=[{'id':i,'naam':r['Onderdeel'],'aantal':r['Aantal'],'prijs':float((r['Prijs 1 (EUR incl. btw)'] or '0').replace(',','.'))} for i,r in enumerate(rows)]
t=(d/'afvinklijst.template.html').read_text()
(d/'afvinklijst.html').write_text(t.replace('/*DATA*/[]',json.dumps(items)))
