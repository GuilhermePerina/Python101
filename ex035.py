#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('=-=-'*20)
print('Vou escolher um número entre 0 e 5')
n=int(randint(0,5))
print('=-=-'*20)

n1=int(input('Qual número você acha que eu escolhi? '))

print('Processando...')
sleep(1)

if n==n1:
    print('Você venceu, esse foi o número que eu pensei!')
else:
    print('Você perdeu, o número que eu pensei foi {}!'.format(n))
