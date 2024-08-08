#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

s1=float(input('Primeiro Segmento: '))
s2=float(input('Segundo Segmento: '))
s3=float(input('Terceiro Segmento: '))

if (s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo!')