# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n=int(input('Digite um numero e lhe darei sua taboada: '))

print('='*15)

for n1 in range(0, 11):
    print('{} x {} = {}'.format(n, n1, n*n1))

print('='*15)
