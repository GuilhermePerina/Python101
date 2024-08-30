# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira


from math import floor
n=float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, floor(n)))


n1=float(input('Digite outro número: '))
n2=n1//1
print('O número {1} tem a parte inteira {0:.0f}'.format(n2, n1))


from math import trunc
n3=float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n3, trunc(n3)))


n4=float(input('Digite outro número: '))
print('O número {} tem a parte inteira {}'.format(n4, int(n4)))
