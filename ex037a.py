a = int(input('Digite o número que vai para decimal:'))
list = []
while a > 2:
    b = a // 2
    c = a % 2
    list.append(c)
    a = b
print(list)
