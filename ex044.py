print('{:*^40}'.format(' LOJAS MICHELAN '))
a = float(input('DIGITE O PREÇO TOTAL DAS COMPRAS: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] À VISTA EM DINHEIRO
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X A 10X OU MAIS NO CARTÃO''')
b = int(input('QUAL É A OPÇÃO???:'))
if b == 1:
    print('SUA COMPRA DE R${:.2f} VAI CUSTAR R${:.2f} NO FINAL'.format(a, a*.9))
elif b == 2:
    print('SUA COMPRA DE R${:.2f} VAI CUSTAR R${:.2f} NO FINAL'.format(a, a*.95))
elif b == 3:
    print('SUA COMPRA SERÁ PARCELADA EM 2X DE R${:.2f} SEM JUROS NO FINAL'.format(a/2))
elif b == 4:
    c = int(input('QUANTIDADE DE PARCELAS:'))
    print('SUA COMPRA SERÁ PARCELADA EM {}X DE R${:.2f} SEM JUROS NO FINAL'.format(c, (a*1.2)/c))
else:
    print('OPÇÃO INVÁLIDA!')
