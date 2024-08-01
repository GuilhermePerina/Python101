# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área 
# de 2 metros quadrados.


alt=float(input('Qual a altura da sua parede? '))
lar=float(input('Qual a largura da sua parede? '))

area=(alt*lar)
tinta=(area/2)

print('A area total da parede é {}m² \nVamos precisar de {} litros de tinta para pintar essa parede'.format(area, tinta))
