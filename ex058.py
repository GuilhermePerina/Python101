# Exercício Python 048: Faça um programa que calcule a soma entre todos os números ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.

count=0
soma=0
for n in range (1, 501, 2):
    if n%3==0:
        soma=soma+n     #ou: soma += n    # um acumulador normalmente soma um valor
        count=count+1   #ou: count +=1    # um contador normalmente soma 1
        #print(n, end=' ')
print('A soma de todos os {} valores solicitados é {}'.format(count, soma))

