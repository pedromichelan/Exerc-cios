#soma de todos o números ímpares / multiplos de 3 / detro de 1 a 500
a = range(1, 501, 2)
b = 0
for x in a:
    if x % 3 == 0:
        b = b + x
        print(x, end=' ')
print('\n')
print('A SOMA TOTAL É {}'.format(b))
print(len(a))
