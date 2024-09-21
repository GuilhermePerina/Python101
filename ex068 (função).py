# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
n=randint(0,10)
count = 1
def timer(segundos, frase): #inventei uma função "timer" usando o "def" pro parâmetro "segundos" receber o valor que o sleep vai receber e o parâmetro "frase" pra receber o que eu escrever dentro da função futuramente
    print('Processando{}'.format(frase))
    sleep(segundos) #esse é o parâmetro que vai ser alterado na função "timer"


print ('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

palpite=int(input('Me manda seu palpite ai: '))

if palpite==n:
        timer(0.5, '...') #o valor que eu colocar no timer vai ser a variável do parâmetro "segundos"
        print('Você acertou de primeira. Parabéns!')
else:
    while palpite!=n:
        timer(0.3, ' novamente...')
        count +=1
        if palpite<n:
            palpite=int(input('Mais... Tente outro número: '))
        if palpite>n:
            palpite=int(input('Menos... Tente outro número: '))
        if palpite==n:
            timer(0.4, '... agora sim!')
            print('Você acertou com {} tentativas.'.format(count))
