# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n=str(input('Digite seu nome completo: ')).strip()
name=n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu último nome é: {}'.format(name[len(name)-1]))
