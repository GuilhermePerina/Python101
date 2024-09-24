#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n=int(input('Digite um número para calcular seu fatorial: '))
n1=n
f=1
for n1 in range (n, 0, -1):
    f*=n1
print('Calculando...')
print('O fatorial de {} = {}'.format(n, f))

#or

from math import factorial
n=int(input('Digite um número para calcular seu fatorial: '))
f=factorial(n)
print('O fatorial de {} é {}'.format(n, f))

#or

n=int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
while c>0:
    print ('{}'.format(c), end='')
    print (' x ' if c> 1 else ' = ', end='')
    f*=c
    c-=1
print('{}'.format(f))
