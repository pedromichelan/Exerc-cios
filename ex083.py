a = str(input('DIGITE A EXPRESSÃO: '))
b = []
for x in a:
    if x == '(':
        b.append('(')
    elif x == ')':
        if len(b) > 0:
            b.pop()
        else:
            b.append(')')
            break
if len(b) == 0:
    print('EXPRESSÃO VÁLIDA!')
else:
    print('EXPRESSÃO INVÁLIDA!')
