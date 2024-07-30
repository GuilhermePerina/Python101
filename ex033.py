frase=str(input('Digite uma frase: ')).strip()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a') + frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.upper().find('A')))
print('A última letra "A" apareceu na posição {}'.format(frase.lower().rfind('a')))
