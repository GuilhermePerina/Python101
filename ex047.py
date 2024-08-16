# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual=date.today().year

nasc=int(input('Ano de nascimento: '))

idade=atual-nasc

print('Quem nasceu em {} tem {} anos em 2024'.format(nasc, idade))

if idade==18:
    print('Você deve se alistar ao Exército Brasileiro IMEDIATAMENTE!')

elif idade>18:
    ha=idade-18
    foi=atual-ha
    print('Você já deveria ter se alistado ao Exército Brasileiro há {} anos!\nSeu alistamento foi em {}'.format(ha, foi))

else:
    faltam=18-idade
    ira=faltam+atual
    print('Ainda faltam {} anos para o alistamento.\nVocê deve se alistar ao Exército Brasileiro em {}!'.format(faltam, ira))
