#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Dica: Se o ano não termina em 00, ele é bissexto caso seja divisível por 4.

from datetime import date

ano=int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
bissexto=ano%4

if ano == 0:
    ano = date.today().year

if bissexto==0 and ano % 100 != 0 or ano%400==0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))

#or

from calendar import isleap

if isleap(ano):
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))