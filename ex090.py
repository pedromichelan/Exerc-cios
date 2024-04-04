print(f'{" SITUAÇÃO DO ALUNO ":-^40}')
a = {}
a['NOME'] = str(input('NOME: '))
a['MÉDIA'] = float(input(f'MÉDIA DE {a["NOME"]}: '))
if a['MÉDIA'] < 6:
    a['SITUAÇÃO'] = 'REPROVADO'
elif 6 <= a['MÉDIA'] < 7:
    a['SITUAÇÃO'] = 'RECUPERAÇÃO'
else:
    a['SITUAÇÃO'] = 'APROVADO'
print('-=-'*15)
for x, y in a.items():
    print(f'- {x} é igual a {y}')
