#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso=float(input('Qual o seu peso? '))
altura=float(input('Qual a sua altura? '))
imc=peso/(altura**2)

print('O seu IMC é {:.1f}'.format(imc))

if imc<18.5:
    print('Você está abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Você está no peso ideal')
elif imc>=25 and imc<30:
    print('Você está acima do peso')
elif 30<=imc<40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')
