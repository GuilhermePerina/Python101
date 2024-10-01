# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

n=int(input('Primeiro termo: '))
razao=int(input('Razão da P.A.: '))
count=1
primeiro=n+razao
proximo=n
mais=10
total=0

print(n, end=' > ')

while mais!=0:
    total+=mais
    while count <= total:
        count+=1
        proximo+=razao
        print(proximo, end=' > ')
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais? '))
print('Finalizamos com um total de {} termos mostrados'.format(count-1))
