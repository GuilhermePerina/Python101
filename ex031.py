# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade=str(input('Digite o nome da cidade onde você mora: \n')).strip()

print('A sua cidade começa com "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))

print('A sua cidade começa com "Santo"? {}'.format('SANTO' in cidade.split()[0].upper()))
