#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase=str(input('Digite uma frase: '))
frasejunta=''.join(frase.split()).strip().upper()

inverso=frasejunta[::-1].strip()

print('o inverso de {} é {}'.format(frasejunta, inverso))

if frasejunta==inverso:
    print('Temos um palíndromo!')
else:
    print('A frase {} não é um palíndromo!'.format(frase))


#or

frase1=str(input('Digite uma frase: ')).strip().upper()
palavras=frase1.split()
junto=''.join(palavras)
inverso1 = ''

for letra in range(len(junto) -1, -1, -1):
    inverso1 += junto[letra]
if inverso1 == junto:
    print('Temos um palíndromo!')
else:
    print('A frase {} não é um palíndromo!'.format(frase1))
