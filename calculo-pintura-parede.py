alt = float(input('Insira a altura da parede: '))
lg = float(input('Insira a largura da parede: '))
area = alt*lg
lts = area/2
print('Para pintar uma parede com {}m² de area é necessário {} litros de tinta.'.format(area, lts))
