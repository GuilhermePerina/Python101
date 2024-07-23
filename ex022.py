import math
n=float(input('Cateto Adjacente: '))
n1=float(input('Cateto Oposto: '))
n2=math.hypot(n, n1)

print('O comprimento da hipotenusa equivale a {:.2f}'.format(n2))
