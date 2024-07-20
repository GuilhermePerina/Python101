
n1 = int(input('Digite um número: '))

pares = []
impares = []

for count in range(n1):
    if(count%2==0):
        pares.append(count)
    else:
        impares.append(count)

opcao = int(input('\nVocê quer ver os números impares ou pares de 0 até {}? Digite 1 para impar e 2 para par: '.format(n1)))

print('\n')
if opcao == 1:
    print(impares)

if opcao == 2:
    print(pares)
    