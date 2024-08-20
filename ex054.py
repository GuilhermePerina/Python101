#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

print('=='*5, 'VAMOS JOGAR JOKENPÔ!', '=='*5)

print('''Opções:
    [1] Pedra
    [2] Papel
    [3] Tesoura''')

escolha=int(input('Digite a opção: '))

if escolha>3 or escolha==0:
    print('Opção inválida!')
else:
    print('JO-KEN-PO!')
    print('--'*20)

    if escolha==1: you='Pedra'
    elif escolha==2: you='Papel'
    elif escolha==3: you='Tesoura'
    print('Sua escolha: {}'.format(you))

    import random
    computer=['Pedra', 'Papel', 'Tesoura']
    computador=random.choice(computer)
    print('Escolha do computador: {}'.format(computador))

    if you=='Pedra' and computador=='Papel' or you=='Papel' and computador=='Tesoura' or you=='Tesoura' and computador=='Pedra':
        print('Eu ganhei!!')
    elif you=='Pedra' and computador=='Tesoura' or you=='Papel' and computador=='Pedra' or you=='Tesoura' and computador=='Papel':
        print('Você ganhou!!')
    else:
        print('Nós empatamos!')

    print('====='*20, '\n')
#or

    from random import randint
    opcoes=('Pedra', 'Papel', 'Tesoura')
#          0         1        2
    computador=randint(0, 2)
    print('''Suas opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
    jogador=int(input('Qual é a sua jogada? '))

    if jogador>2:
        print('Esta não é uma opção válida!')
    else:
        print('Sua escolha: {}'.format(opcoes[jogador]))
        print('Minha escolha: {}'.format(opcoes[computador]))

        if jogador==computador:
            print('Empatamos')
        elif jogador==0 and computador==1 or jogador==1 and computador==2 or jogador==2 and computador==0:
            print('Eu ganhei!')
        else:
            print('Você ganhou!')
