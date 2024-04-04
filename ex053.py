print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m     IDENTIFICADOR DE POLÍNDROMO \033[m')
print('\033[1;31;46m==\033[m'*20)
a = str(input('DIGITE UMA FRASE:').strip().upper())
print('VOCÊ DIGITOU A FRASE: {}'.format(a))
b = a.split()
c = ''.join(b)
d = []
for x in range(len(c)-1, -1, -1):
        d.append(c[x])
dj = ''.join(d)
print('{} ao contrário é {}'.format(c, dj))
if c == dj:
    print('É PALÍNDROMO!')
else:
    print('NÃO É PALÍNDROMO')
