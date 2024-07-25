frase='Curso em Vídeo Python'

print('Na frase:', frase, '\n\n')

print('Ferramentas de Análise', '\n')
print('Quero saber quantas casas tem a frase:', len(frase))
print("Quero saber quantas letras 'o' tem na frase:", frase.count('o'))
print("Quero saber quantas letras 'o' tem da casa 0 até a casa 13:", frase.count('o',0, 13))
print("Quero saber se tem e onde começa 'deo' na frase:", frase.find('deo'), '\n\n')

print('Ferramentas de Fatiamento', '\n')
print('Quero saber o que tem na casa 9:', frase[9])
print('Quero somente o que começa na casa 9, vai até a casa 21:', frase[9:21])
print('Quero somente o que começa na casa 15 e vai até o final:', frase[15:])
print('Quero somente o que começa no zero e vai até a casa 5:', frase[:5])
print('Quero somente o que começa na casa 9, vai até a casa 21, pulando de 2 em 2 casas:', frase[9:21:2])
print('Quero somente o que começa na casa 9, vai até o final, pulando de 3 em 3 casas:', frase[9::3])
print('Quero somente o que começa na casa 9, vai até a casa 21, pulando de 2 em 2 casas:', frase[9:21:2], '\n\n')

print('Ferramentas de Transformação (lista de strings são imutáveis)', '\n')
print("Quero saber se tem e onde começa 'deo' na frase:", frase.replace('Python', 'Android'))
print("Quero todas as letras da frase maiúsculas:", frase.upper())
print("Quero todas as letras da frase minúsculas:", frase.lower())
print("Quero todas somente a primeira palavra com a primeira letra maiúscula:", frase.capitalize())
print("Quero todas as primeiras letras de cada palavra maiúsculas:", frase.title())
print("Quero que tire todos os espaços antes e depois da frase completa:", frase.strip())
print("Quero que tire todos os espaços somente depois da frase completa:", frase.rstrip())
print("Quero que tire todos os espaços somente antes da frase completa:", frase.lstrip(), '\n\n')

print('Ferramentas de Divisão', '\n')
print("Quero dividir cada palavra em uma nova lista (dividir uma string em uma lista de palavras):", frase.split(), '\n\n')

print('Ferramentas de Junção', '\n')
print("Quero juntar todas as palavras através de um '-':", '-'.join(frase))
