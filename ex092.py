from datetime import date
a = {}
while True:
    a['NOME'] = str(input('NOME: '))
    a['IDADE'] = date.today().year - int(input('ANO DE NASCIMENTO: '))
    a['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM):'))
    if a['CTPS'] == 0:
        break
    a['CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    a['SALÁRIO'] = int(input('SALÁRIO: '))
    a['APOSENTADORIA'] = (a['CONTRATAÇÃO']+35)-(date.today().year - a['IDADE'])
    break
for x, y in a.items():
    print(f'{x} = {y}')
