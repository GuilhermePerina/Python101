n=str(input('Digite seu nome completo: ')).strip()
name=n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu último nome é: {}'.format(name[len(name)-1]))
#
