#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal=float(input('Qual é o salário do funcionário? R$ '))
a1=(sal)+sal*0.15
a2=sal*1.1

if sal<=1250:
    print('O seu novo salário será de {} com o aumento de 15%'.format(a1))
else:
    print('O seu novo salário será de {} com o aumento de 10%'.format(a2))