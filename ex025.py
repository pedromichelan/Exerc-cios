a = str(input('Digite seu nome:')).strip()
a1 = a.lower()
a2 = a1.split()
b = 'silva'
print('Seu nome tem Silva?')
if b in a2:
    print(True)
else:
    print(False)
