#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n=int(input('Digite um número para calcular seu fatorial: '))
fat=0
mult=0
for n1 in range (n, 1, -1):
    fat=fat*(n1*(n1-1))
    mult=mult*(n1-1)
    print(n1)
    print(fat)
    print(mult)
    print('===')
#print('Calculando...')
#print('O fatorial de {} = {}'.format(n, fat))
