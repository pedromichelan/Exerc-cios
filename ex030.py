a = int(input('\033[0;35mDIGITE UM NÚMERO INTEIRO QUALQUER:\033[m'))
b = a/2
c = a//2
if b == c:
    print('\033[36mO NÚMERO {} é:\033[m \033[1;34m PAR\033[m'.format(a))
else:
    print('\033[36mO NÚMERO {} é:\033[m \033[1;34m ÍMPAR\033[m'.format(a))
