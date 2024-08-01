# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random
name=input('Qual é o 1º aluno participante? ')
name1=input('Qual é o 2º aluno participante? ')
name2=input('Qual é o 3º aluno participante? ')
name3=input('Qual é o 4º aluno participante? ')
names=[name, name1, name2, name3]

sorteio=random.choice(names)

print('O sorteado foi {}'.format(sorteio))