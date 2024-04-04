from math import hypot
a = float(input('Digite o cateto oposto:'))
b = float(input('Digite o cateto adjacente:'))
c = pow((a**2+b**2), 0.5)
print('A hipotenusa mede {:.2f}'.format(c))
print('Hipotenusa é {}'.format(hypot(a,b)))
