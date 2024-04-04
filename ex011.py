a = float(input('Largura da parede:'))
b = float(input('Altura da parede'))
#consumo
c = 0.5
print('Sua parede tem dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m²'.format(a, b, a*b))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(a*b*c))
