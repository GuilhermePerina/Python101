# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.



import math
n=float(input('Cateto Adjacente: '))
n1=float(input('Cateto Oposto: '))
n2=math.hypot(n, n1)

print('O comprimento da hipotenusa equivale a {:.2f}'.format(n2))


ca=float(input('Cateto Adjacente: '))
co=float(input('Cateto Oposto: '))
hi=(co**2+ca**2)**(1/2)

print('A hipotenusa equivale a {:.2f}'.format(hi))
