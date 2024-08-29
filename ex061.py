#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('--'*20)
print('10 Termos de uma PA')
print('--'*20)

termo=int(input('Primeiro Termo: '))
razao=int(input('Razão: '))
primeiro=termo+razao
proximo=termo

print(termo, end=' > ')
for n in range (1, 10):
    proximo+=razao
    print(proximo, end=' > ')
print('Acabou\n')

#or

primeiro=int(input('Primeiro Termo: '))
razao1=int(input('Razão: '))
decimo=primeiro+(10-1)*razao1

for c in range (primeiro, decimo + razao1, razao1):
    print(c, end=' > ')
print('Acabou')