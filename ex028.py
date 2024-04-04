from colorama import init, Fore, Back
init()
print((Fore.YELLOW + '-=-')*20)
print(Fore.WHITE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(Fore.YELLOW + '-=-'*20)
a = int(input(Fore.WHITE +'Em que número eu pensei?'))
print(Fore.WHITE +'PROCESSANDO...')
from time import sleep
sleep(3)
from random import choice
b = [1, 2, 3, 4, 5]
c = choice(b)
if a == c:
    print(Fore.WHITE +'ACERTOU!')
else:
    print(Fore.WHITE +'ERROU! Eu pensei no número {}'.format(c))
