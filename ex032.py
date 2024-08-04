# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome=input('Qual seu nome? \n').strip()

hasSilva='silva' in nome.lower()

if hasSilva:
    print('Sim! Você tem Silva no nome')
else:
    print('Não! Você não tem Silva no nome')
