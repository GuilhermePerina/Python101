print('oi' + 'ola', '\n')
print('oi'*5, end='')
print ('='*20)
 
name=input('Qual seu nome? ')
print('Seja bem vindo, {}!'.format(name))
print('Seja bem vindo, {:20}!'.format(name))
print('Seja bem vindo, {:<20}!'.format(name))
print('Seja bem vindo, {:>20}!'.format(name))
print('Seja bem vindo, {:^20}!'.format(name))
print('Seja bem vindo, {:=^20}!'.format(name))
