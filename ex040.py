print('\033[1;33m-=-\033[m'*12)
print('    ANÁLISE DE NOTAS DE UM ALUNO')
print('\033[1;33m-=-\033[m'*12)
a = float(input('DIGITE A PRIMEIRA NOTA DO ALUNO: '))
b = float(input('DIGITE A SEGUNDA NOTA DO ALUNO: '))
c = (a+b)/2
print('UM ALUNO COM AS NOTAS {:.1f} E {:.1f} TEM A MÉDIA {:.1f}'.format(a, b, c))
if c < 5:
    print('ALUNO REPROVADO!')
elif c >= 7:
    print('ALUNO APROVADO!')
else:
    print('ALUNO DE RECUPERAÇÃO!')
