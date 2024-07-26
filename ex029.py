nome=str(input('Me diga seu nome: \n')).strip()

print(nome.upper(), ': com todas as letras Maiúsculas')
print(nome.lower(), ': com todas as letras Minúsculas')
print(nome, ': tem {} caracteres ao todo'.format(len(nome)))
print(nome, ': tem {} letras ao todo, sem considerar os espaços'.format(len(nome) - nome.count(' ')))
print(nome, ': seu primeiro nome tem {} letras'.format(nome.find(' ')))

nome2=nome.split()
nome3=''.join(nome2)

print(nome, ': tem {} letras ao todo, sem considerar os espaços'.format(len(nome3)))
print(nome, ': seu primeiro nome tem {} letras'.format(len(nome2[0])))
