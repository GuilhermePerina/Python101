#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(0, 51, 2):
    print(c, end=' ')

print('')
print('==='*20, '\n')


#or


for c in range(1,51):
    if c%2==0:
        print(c, end=' - ')
print('')

# Na primeira opção o computador só faz o cálculo de 2 em 2 números
# Na segunda opção o computador tem que calcular número por número pra saber o resultado
# Usando a primeira opção, usamos metade da CPU, porque os cálculos foram pela metade, fazendo o programa ficar mais leve e mais eficiente
# imagine como uma pessoa indo buscar sacos de areia, e você dizendo pra só pegar o saco se estiver com algo dentro, isso vai fazer a pessoa ir até o local pra olhar o saco todas as vezes, pra só pegar quando tiver algo dentro, fazendo gastar energia atoa só pra ir la olhar o saco primeiro.

