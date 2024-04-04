from math import sin, cos, tan, radians
a = float(input('Digite o ângulo do qual deseja saber as informações:'))
print('O sendo de {:.2f}° é {:.2f} o cosseno de {:.2f}° é {:.2f} a tangente de {:.2f}° é {:.2f}'.format(a, sin(radians(a)), a, cos(radians(a)), a, tan(radians(a))))
