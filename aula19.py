'''pessoas = {'NOME': 'PEDRO', 'SEXO': 'M', 'IDADE': 22 }
print(pessoas['NOME'])
print(f'O {pessoas["NOME"]} TEM {pessoas["IDADE"]} ANOS')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['NOME'] = 'ANDRÉ'
pessoas['PESO'] = 85
for x, y in pessoas.items():
    print(f'{x} = {y}')'''
'''a = {'UF':'PARANÁ', 'SIGLA':'PR'}
b = {'UF':'SANTA CATARINA', 'SIGLA':'SC'}
c = []
c.append(a)
c.append(b)
print(c[0]['UF'])'''
a = [['jaca', 10, 'doce'], ['abobora', 12, 'salgada']]
for i, x in enumerate(a):
    print(f'{i}, {x[0]}, {x[1]}, {x[2]}')
