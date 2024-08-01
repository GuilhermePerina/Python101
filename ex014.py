# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# mostre quantos dólares ela pode comprar.


real=int(input('Quantos reais você tem na carteira? \nR$ '))
dol=real/5.45

print('Com R$ {} reais você consegue comprar US$ {} dolares'.format(real, "%.2f" %dol))
