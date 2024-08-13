#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

limpa={'limpa':'\033[m'}

s={'none': '\033[0m',
   'bold': '\033[1m',
   'underline': '\033[4m',
   'negative': '\033[7m'
   }

t={'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m'
    }

b={'branco': '\033[40m',
   'vermelho': '\033[41m',
   'verde': '\033[42m',
   'amarelo': '\033[43m',
   'azul': '\033[44m',
   'roxo': '\033[45m',
   'ciano': '\033[46m',
   'cinza': '\033[47m'
   }

print('\n')
print(s['underline'], 'Digite 3 valores de segmentos de um triângulo', s['none'], '\n')

s1=float(input('\033[41mPrimeiro Segmento: \033[m'))
s2=float(input('\033[42mSegundo Segmento: \033[m'))
s3=float(input('\033[43mTerceiro Segmento: \033[m'))

print('\n')
if (s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1:
    print('{}Os segmentos acima {}podem{}{} formar um triângulo{}'.format(t['verde'], b['verde'], limpa['limpa'], t['verde'], limpa['limpa']))
else:
    print('{}Os segmentos acima {}não podem{}{} formar um triângulo!{}'.format(t['vermelho'], b['vermelho'], limpa['limpa'], t['vermelho'], limpa['limpa']))
    