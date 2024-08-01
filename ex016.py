# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preço=float(input('Qual é o preço do produto? '))
desc=preço-(preço*5/100)

print('Seu novo preço agora é {} com 5% de desconto'.format("%.2f" %desc))

print('-'*60)

preço2=float(input('Qual é o preço do produto? '))
desc2=(preço2/1.05)

print('Seu novo preço agora é {} com 5% de desconto'.format("%.2f" %desc2))
