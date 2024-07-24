## Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


x = input ('Digite algo: ')
print('qual é o tipo primitivo de {}?'.format(x), type(x))
print('"{}" tem caractere US-ASCII de 7–bit válido?'.format(x), x.isascii())
print('"{}" tem uma letra ou um número?'.format(x), x.isalnum())
print('"{}" tem uma letra?'.format(x), x.isalpha())
print('Todos os caracteres de "{}", são dígitos decimais?'.format(x), x.isdecimal())
print('Todos os caracteres de "{}", são dígitos?'.format(x), x.isdigit())
print('"{}" é um identificador válido de acordo com a definição da linguagem Python?'.format(x), x.isidentifier())
print('"{}" só tem letras minúsculas?'.format(x), x.islower())
print('"{}" é imprimível?'.format(x), x.isprintable())
print('"{}" está no formato de título? (primeira letra de cada palavra em maiúsculo)'.format(x), x.istitle())
print('"{}" só tem letras maiúsculas?'.format(x), x.isupper())
print('"{}" é um número?'.format(x), x.isnumeric())
print('"{}" é somente espaços?'.format(x), x.isspace())
