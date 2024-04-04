print('\033[1;31;46m==\033[m'*15)
print('\033[1;37m  LOJAS SUPER BARATÃO \033[m')
print('\033[1;31;46m==\033[m'*15)
c = 0 #somador de valores totais
d = 0 #contador de produtos acima de R$1.000,00
e = ' ' #produto mais barato
f = 0 #valor mais barato
g = 0 #contador de produtos
while True:
    g += 1
    a = str(input('NOME DO PRODUTO: '.strip().upper()))
    b = float(input('VALOR DO PRODUTO: R$'))
    if g == 1:
        e = a
        f = b
    c += b
    if b > 1000:
        d += 1
    if b < f:
        e = a
        f = b
    h = ' '
    while h not in 'SN':
        h = str(input('DESEJA CONTINUAR? [S/N]: ').strip().upper()[0])
    if h == 'N':
        break
print(f'O TOTAL DA COMPRA FOI R${c:.2f}')
print(f'TEMOS {d} PRODUTOS CUSTANDO ACIMA DE R$1.000,00')
print(f'O PRODUTO MAIS BARATO FOI {e} QUE CUSTA {f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
