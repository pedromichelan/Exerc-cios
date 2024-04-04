print(f'{" ANALISADOR DE PESSOAS ":-^40}')
a = []
b = {}
while True:
    b['NOME'] = str(input('NOME: '))
    b['SEXO'] = ' '
    while b['SEXO'] not in 'MF':
        b['SEXO'] = str(input('SEXO [M/F]: ').strip().upper()[0])
        if b['SEXO'] not in 'MF':
            print('ERRO! POR FAVOR, DIGITE APENAS M OU F.')
    b['IDADE'] = int(input('IDADE: '))
    a.append(b.copy())
    c = ' '
    while c not in 'SN':
        c = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
        if c not in 'SN':
            print('ERRO! POR FAVOR, DIGITE APENAS S OU N')
    if c == 'N':
        break
d = 0
for x in range(0, len(a)):
    d += a[x]['IDADE']
print(f'A) AO TODO TEMOS {len(a)} PESSOAS CADASTRADAS.')
print(f'B) A MÉDIA DE IDADE É DE {d/len(a)} ANOS.')
print('C) AS MULHERES CADASTRADAS FORAM: ', end='')
for x in a:
    if x['SEXO'] == 'F':
        print(f'{x["NOME"]}', end=' ')
print('\nD) LISTA DAS PESSOAS ACIMA DA MÉDIA DE IDADE:')
for x in a:
    if x['IDADE'] > (d/len(a)):
        print(f'NOME = {x["NOME"]}; SEXO = {x["SEXO"]}; IDADE = {x["IDADE"]}')
print('ENCERRADO')
