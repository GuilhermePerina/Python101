#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase=str(input('Digite uma frase: '))
frasejunta=''.join(frase.split())

inverso=frasejunta[::-1].strip()

print('o inverso de {} é {}'.format(frasejunta, inverso))

if frasejunta==inverso:
    print('Temos um palíndromo!')
else:
    print('A frase {} não é um palíndromo!'.format(frase))