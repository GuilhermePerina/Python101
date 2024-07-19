#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

n1=float(input('Quantos quilômetros o carro percorreu? '))
n2=float(input('Por quantos dias foi alugado? '))

print('O total a pagar é R$ {}'.format((60*n2)+(n1*0.15)))
