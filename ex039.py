import datetime

print('\033[1;33m-=-\033[m'*12)
print('        ALISTAMENTO MILITAR')
print('\033[1;33m-=-\033[m'*12)
from datetime import date
print('ESTAMOS NO ANO {}'.format(datetime.date.today().year))
a = int(datetime.date.today().year)
b = int(input('DIGITE O ANO SE SEU NASCIMENTO: '))
print('ESTE ANO VOCÊ COMPLETA OU COMPLETOU {} ANOS.'.format(a - b))
if a - b < 18:
    print('VOCÊ DEVERÁ SE ALISTAR EM {}'.format(b+18))
    ano = 10
elif a - b > 18:
    print('VOCÊ ESTÁ EM DÉBITO. DEVERIA TER SE ALISTADO EM {}! PRUCURE A JUNTA MILITAR!'.format(b+18))
else:
    print('VOCÊ DEVE SE ALISTAR ESSE ANO! PROCURE A JUNTA MAIS PRÓXIMA!')
print(ano)
