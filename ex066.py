# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma=0
maisVelho=0
homemMaisVelho=0
count=0

for p in range (1,5):
    print ('-'*5, '{}ª Pessoa'.format(p),'-'*5)
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()

    soma+=idade

    if sexo=='M' or sexo=='m':
        if maisVelho<idade:
            maisVelho=idade
            homemMaisVelho=nome
    elif sexo in 'Ff' and idade<20:
        count+=1

print('A média de idade do grupo é de {} anos.'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisVelho, homemMaisVelho))
print('Ao todo são {} mulheres com menos de 20 ano.'.format(count))
