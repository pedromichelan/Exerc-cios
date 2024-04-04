a = str(input('Se começar com Santo será "True"\nEm que cidade você nasceu?')).strip()
a1 = str(a.lower())
a2 = a1.split()
b = 'santo'
if a2[0] == b:
    print(True)
else:
    print(False)
print(a1)
