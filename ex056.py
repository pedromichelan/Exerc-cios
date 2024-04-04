print('\033[1;31;46m==\033[m'*20)
print('\033[1;37m           ANÁLISE PESSOAS \033[m')
print('\033[1;31;46m==\033[m'*20)
a = 0 #soma idade
b = 0 #conta idade
c = 0 #idade homem mais velho
d = '' #nome homem mais velho
e = 0 # soma mulheres menores de 20 anos
for x in range(1, 5):
    print('---- {}ª PESSOA ----'.format(x))
    nome = str(input('NOME: '.upper().strip()))
    idade = float(input('IDADE: '.upper()))
    sexo = str(input('SEXO [M/F]: '.upper().strip()))
    a = a + idade
    b = b + 1
    if sexo == 'M':
       if idade > c:
            c = idade
            d = nome
    if sexo == 'F':
        if idade < 20:
            e = e + 1
print('A MÉDIA DE IDADE DO GRUPO É DE {} ANOS'.format(a/b))
print('O HOMEM MAIS VELHO TEM {} ANOS E SE CHAMA {}'.format(c, d))
print('AO TODO SÃO {} MULHERES COM MENOS DE 2O ANOS'.format(e))
