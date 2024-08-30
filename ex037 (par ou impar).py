#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n=int(input('\033[0;32;46mMe diga um número qualquer: \033[m'))
resto=n%2

if resto==0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))
