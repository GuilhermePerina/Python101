#Código para verificar se um número é par ou impar
n1 = int(input('Digite um número: '))
repeat = True

while repeat:
    if n1%2==0:
        print('O número {} é par \n'.format(n1))
    else:
        print('O número {} é impar. \n'.format(n1))

    again = input('Quer digitar outro número? ')

    if again == 'Sim':
        n1 = int(input('Digite outro número: '))
    elif again == 'Não':
        print('Obrigado por participar!\n')
        repeat = False
    else:
        print('Este é não é um comando válido \n Digite Sim ou Não')
        n1 = input('Quer digitar outro número? ')
