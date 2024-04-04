print('\033[1;33m-=-\033[m'*12)
print('  CLASSIFICADOR DE MASSA CORPÓREA')
print('\033[1;33m-=-\033[m'*12)
a = float(input('DIGITE O PESO DA PESSOA: '))
b = float(input('DIGITE A ALTURA DA PESSOA: '))
c = a/(b**2)
print('O IMC DA PESSOA ANALISADA É {:.1f}'.format(c))
if c < 18.5:
    print('A PESSOA ANALISADA ESTÁ ABAIXO DO PESO RECOMENDADO!')
elif 18.5 <= c < 25:
    print('A PESSOA ANALISADA ESTÁ DENTRO DA FAIXA DE PESO RECOMENDADA!')
elif 25 <= c < 30:
    print('A PESSOA ANALISADA ESTÁ COM SOBREPESO!')
elif 30 <= c < 40:
    print('A PESSOA ANALISADA ESTÁ COM OBESIDADE!')
elif 40 <= c:
    print('A PESSOA ANALISADA ESTÁ COM OBESIDADE MÓRBIDA!')
