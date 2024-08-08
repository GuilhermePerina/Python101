# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

um=float(input('\033[1;32mPrimeiro Valor: '))
dois=float(input('\033[1;31mSegundo Valor: '))
tres=float(input('\033[1;33mTerceiro Valor: '))

print('\033[m\n')

numeros = [um, dois, tres]

print('\033[4;44mO menor valor digitado foi {}\033[m'.format(min(numeros)))
print('\033[4;45mO maior valor digitado foi {}\033[m'.format(max(numeros)), '\n')

print('\033[7m==--'*20, '\n\33[m')

#ou

lista = sorted(numeros)

print('\33[41mO menor número é {}\33[m'.format(lista[0]))
print('\33[42mO maior número é {}\33[m'.format(lista[2]), '\n')

print('\033[7m==--'*20, '\n\33[m')

#ou

if um<dois and um<tres:
    menor=um
if dois<um and dois<tres:
    menor=dois
if tres<um and tres<dois:
    menor=tres

maior=um
if dois>um and dois>tres:
    maior=dois
if tres>um and tres>dois:
    maior=tres
    
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior), '\n')

print('\033[7m==--'*20, '\n\33[m')
