# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# (é divisível apenas por um e por ele mesmo)

n=int(input('Digite um número: '))
count=0
for i in range(1, n+1):
    #print(i, end=' ')
    if n%i==0:
        count+=1
        print(i, end=' ')
print('')
if n==1:
    print('O número {} NÃO é primo!'.format(n))
elif count<=2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} NÃO é primo!'.format(n))
print('')
