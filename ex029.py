from colorama import init, Fore, Back
a = int(input('Digite a velocidade atual do seu carro:'))
b = 80
c1 = (a-b)*7
c = str('R${:.2f}'.format(c1))
init()
if a <= b:
    print(Fore.CYAN + 'TENHA UM BOM DIA! DIRIJA COM SEGURANÇA!')
else:
    print(Fore.RED + 'MULTADO! VOCÊ EXCEDEU O LIMITE DE \033[1;33m{}KM/H\033[m. \nVOCÊ DEVE PAGAR UMA MULTA DE \033[1;33m{}\033[m'.format(b, c))
