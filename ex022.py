a = str(input('Digite seu Nome:')).strip()
maiusc = a.upper()
minusc = a.lower()
b = len(a)
c = 1
d = {1:'aa', 2:'bb', 3:'cc', 4:'dd', 5:'ee'}
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(maiusc))
print('Seu nome em minúsculas é: {}'.format(minusc))
print('Seu nome tem {} letras.'.format(b-a.count(' ')))
print('Seu primeiro nome tem {} letras'.format(a.find(' ')))
separa = a.split()
print(separa)
print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
