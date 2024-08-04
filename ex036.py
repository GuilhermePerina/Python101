#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


vel=float(input('Digite a velocidade do carro: '))

multa=float((vel-80)*7)

if vel>80:
    print('Você foi multado em R$ {} por excesso de velocidade! Dirija com cuidado!'.format(multa))

else:
    print('Parabéns! Continue andando na velocidade permitida pela via')
