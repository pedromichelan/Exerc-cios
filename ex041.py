print('\033[1;33m-=-\033[m'*14)
print('     CLASSIFICAÇÃO ETÁRIA DE ATLETAS')
print('\033[1;33m-=-\033[m'*14)
a = int(input('DIGITE O ANO DE NASCIMENTO DO ATLETA:'))
from datetime import date
b = int(date.today().year)
c = b - a
if c<=9:
    print('ATLETA MIRIM! O ATLETA TEM {} ANOS!'.format(c))
elif 9 < c <= 14:
    print('ATLETA INFANTIL! O ATLETA TEM {} ANOS!'.format(c))
elif 14 < c <= 19:
    print('ATLETA JUNIOR! O ATLETA TEM {} ANOS!'.format(c))
elif 19 < c <=  25:
    print('ATLETA SÊNIOR! O ATLETA TEM {} ANOS!'.format(c))
elif c > 25:
    print('ATLETA MASTER! O ATLETA TEM {} ANOS!'.format(c))
