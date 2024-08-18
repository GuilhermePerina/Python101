# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

s1=float(input('Primeiro segmento: '))
s2=float(input('Segundo segmento: '))
s3=float(input('terceiro segmento: '))

print('')
if (s1+s2)>s3 and (s2+s3)>s1 and (s1+s3)>s2:
    print('Os 3 segmentos podem formar um triângulo')
    if s1==s2 and s2==s3:
        print('Este triângulo é EQUILÁTERO')
    elif s1==s2 and s1!=s3 or s2==s3 and s2!=s1 or s1==s3 and s1!=s2:
        print('Este triângulo é ISÓSCELES')
    elif s1!=s2 and s2!=s3 and s1!=s3:
        print('Este triângulo é ESCALENO')
else:
    print('Os 3 segmenos não podem formar um triângulo')
