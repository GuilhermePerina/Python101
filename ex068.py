# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
n=randint(0,10)

print ('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

palpite=int(input('Me manda seu palpite ai: '))

if palpite==n:
        print('Você acertou de primeira. Parabéns!')
else:
    while palpite!=n:
        if palpite<n:
            novamente=int(input('Mais... Tente outro número: '))
        if palpite>n:
            novamente=int(input('Menos... Tente outro número: '))
        if palpite==n:
            print('Você acertou com algumas tentativas.')


#for tentativas in range (0, 10):

















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
