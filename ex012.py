#Exercício Python 008: 
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


v1=float(input('Qual a metragem? '))
v2=(v1*100)
v3=(v2*100)

print('Serão {} centímetros e {} milímetros'.format(round(v2), round(v3)))


