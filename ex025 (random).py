# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
name=input('Qual é o 1º aluno? ')
name1=input('Qual é o 2º aluno? ')
name2=input('Qual é o 3º aluno? ')
name3=input('Qual é o 4º aluno? ')
names=[name, name1, name2, name3]

sorteio=random.sample(names, 4)

print('A ordem de apresentação será {}'.format(sorteio))

#ou

sorteio2=random.shuffle(names)

print('A ordem de apresentação será {}'.format(names))