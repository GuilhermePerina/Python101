# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiores=0
menores=0
for anos in range (1, 8):
    ano=int(input('Em que ano a {}ª pessoa nasceu? '.format(anos)))
    idade=date.today().year-ano
    if idade>=18:
        maiores += 1
    else:
        menores += 1
print('Ao todo são {} pessoas maiores de idade e {} menores de idade!'.format(maiores, menores))
