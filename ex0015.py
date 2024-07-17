alt=float(input('Qual a altura da sua parede? '))
lar=float(input('Qual a largura da sua parede? '))

area=(alt*lar)
tinta=(area/2)

print('A area total da parede é {}m² \nVamos precisar de {} litros de tinta para pintar essa parede'.format(area, tinta))
