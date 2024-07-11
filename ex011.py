name=input('Qual o nome do aluno? ')
nota1=float(input('Sua primeira nota foi: '))
nota2=float(input('Sua segunda nota foi: '))
media=float((nota1+nota2)/2)

print('As duas notas do {} foram {} e {}\nSua média foi {}'.format(name, nota1, nota2, media))
