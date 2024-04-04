print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m      ANÁLISE GRUPO MAIORIDADE \033[m')
print('\033[1;31;46m==\033[m'*20)
a = [ ] #lista de anos de nascimento
for x in range(1, 8):
    a.append(int(input('EM QUE ANO A {}ª PESSOA NASCEU?:'.format(x))))
print(a)
from datetime import date
b = date.today().year
c = 0 #contador menores de idade
d = 0 #contador maiores de idade
for y in a:
    if b - y >= 18:
        d = d + 1
    elif b - y < 18:
        c += 1
print('AO TODO TIVEMOS {} PESSOAS MAIORES DE IDADE'.format(d))
print('AO TODO TIVEMOS {} PESSOAS MENORES DE IDADE'.format(c))
