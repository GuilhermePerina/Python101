# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print ('''Gerador de P.A.
================''')

n=int(input('Primeiro termo: '))
razao=int(input('Razão da P.A.: '))
count = 0
primeiro=n+razao
proximo=n

print(n, end=' > ')

while count < 9:
    count+=1
    proximo+=razao
    print(proximo, end=' > ')
    if count>8:
        print('FIM')    


#or

primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão: '))
termo = primeiro
count = 1

while count <= 10:
    print('{} > '.format(termo), end='')
    termo+=razao
    count+=1
print('FIM')
