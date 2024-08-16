#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date

nasc=int(input('Ano de nascimento: '))
idade=date.today().year-nasc

if idade<10:
    print(f'Você tem {idade} anos de idade e pertence a categoria: Mirim')
elif idade<15:
    print(f'Você tem {idade} anos de idade e pertence a categoria: Infantil')
elif idade<20:
    print(f'Você tem {idade} anos de idade e pertence a categoria: Junior')
elif idade<26:
    print(f'Você tem {idade} anos de idade e pertence a categoria: Senior')
else:
    print(f'Você tem {idade} anos de idade e pertence a categoria: Master')
    