
import random
from time import sleep

print("\nVamos jogar joken-po?\n")
userOption = str(input("Faça sua escolha: ")).strip().lower()

sleep(1)
print("Processando...")
print('\n')
sleep(2)
options=['pedra', 'papel', 'tesoura']
pcOption= random.choice(options)

print('COMPUTADOR           VOCÊ')
print(f'  {pcOption}      x      {userOption}\n')

if pcOption == userOption:
    print('         Empatamos!')
elif userOption=='pedra' and pcOption=='tesoura' or userOption=='papel' and pcOption=='pedra' or userOption=='tesoura' and pcOption=='papel':
    print('         Você ganhou!')
else:
    print('         Eu ganhei!')

print('\n\n--------fim-------\n\n')
