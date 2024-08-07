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

print('O menor número é {}'.format(lista[0]))
print ('O maior número é {}'.format(lista[2]))
