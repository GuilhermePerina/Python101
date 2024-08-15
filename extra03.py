
import random
from time import sleep

print("\nVamos jogar joken-po?\n")

userOption = str(input("Faça sua escolha: ")).strip().lower()

print("Processando...")
sleep(1)
print('\n')
sleep(2)
options=['pedra', 'papel', 'tesoura']
pcOption= random.choice(options)

print('COMPUTADOR           VOCÊ')

if pcOption == userOption:
    print(f'  {pcOption}      x      {userOption}\n')
    print('         Empatamos!')
elif userOption=='pedra' and pcOption=='tesoura' or userOption=='papel' and pcOption=='pedra' or userOption=='tesoura' and pcOption=='papel':
    print(f'  {pcOption}      x      {userOption}\n')
    print('         Você ganhou!')
else:
    print(f'  {pcOption}      x      {userOption}\n')
    print('         Eu ganhei!')

print('\n\n--------fim-------\n\n')