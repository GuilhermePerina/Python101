real=int(input('Quantos reais você tem na carteira? \nR$ '))
dol=real/5.45

print('Com R$ {} reais você consegue comprar US$ {} dolares'.format(real, "%.2f" %dol))
