# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
# com 15% de aumento.


sal=float(input('Qual o salário do funcionário? '))
aumento=(sal*1.15)

print('Com o aumento de 15%, seu novo salário agora será de {}'.format(aumento))

print('='*50)

salario=float(input('Qual é o seu salário? \nR$ '))
novo=salario+(salario*15/100)

print('Seu novo salário agora será de R$ {}'.format(novo))
