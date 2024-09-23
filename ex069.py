#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
primeiro=int(input('Primeiro valor: '))
segundo=int(input('Segundo valor: '))
opcao=0

while opcao!=5:
    print('''===== Menu =====
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')

    opcao=int(input('>>> Escolha uma opção: '))

    if opcao==1:
        soma=primeiro+segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, soma))
    elif opcao==2:
        produto=primeiro*segundo
        print('A multiplicação entre {} X {} é {}'.format(primeiro, segundo, produto))
    elif opcao==3:
        if primeiro>segundo:
            print('O maior número é o primeiro ({})'.format(primeiro))
        elif segundo>primeiro:
            print('O maior número é o segundo ({})'.format(segundo))
        else:
            print('Os dois números são iguais')
    elif opcao==4:
        primeiro=int(input('Primeiro valor: '))
        segundo=int(input('Segundo valor: '))
    elif opcao==5:
        print('='*20)
        print('Fim do programa')
        print ('='*20)
    else:
        print('Opção inválida! Tente novamente.')

    sleep(1)


