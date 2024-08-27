# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('Digite 6 números inteiros')
soma = 0
count = 0
soma2 = 0
count1 = 0
count2 = 0
for c in range(1, 7):
    n=int(input('Número {}: '.format(c)))
    count=count+1
    if n%2==0:
        soma=soma+n
        count1=count1+1
    else:
        soma2=soma2+n
        count2=count2+1
print('Você informou {} números, sendo {} números pares e {} números impares'.format(count, count1, count2))
print('A soma dos números pares da: {}'.format(soma))
print('A soma dos números ímpares da: {}'.format(soma2))
