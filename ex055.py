for c in range(1,11):
    print('Oi')
print('')
print('A palavra "Oi" apareceu 10 vezes (1 do range não conta porque começa a contar do 0)')
print('')
print('=+='*20,'\n')

for yeah in range(0,11):
    print(yeah)
print ('')
print('-=-'*20, '\n')
print ('')

for iha in range(10,0, -1):
    print(iha)
print ('')
print('-=-'*20, '\n')
print ('')

#or

for uow in range(0,10, 2):
    print(uow)
print ('')
print('-=-'*20, '\n')
print ('')

#or

i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for count in range(i, f, p):
    print(count)
print ('')
print('-=-'*20, '\n')
print ('')

#or

s=0
for soma in range (0,4):
    n=int(input('Digite um valor: '))
    s=s+n
print('O somatório de todos os valores foi {}'.format(s))
print('FIM')