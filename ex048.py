#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
media=(n1+n2)/2

print('Tirando {} e {}, a sua média foi de {}'.format(n1, n2, media))

if media>=7:
    print('Você foi aprovado!')
elif media>5 and media<7: #or 7>media>=5
    print('Você está de recuperação!')
else:
    print('Infelizmente você foi reprovado!')
