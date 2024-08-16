#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\33[41mVamos converter números!\033[m')
n1=int(input('\n\033[47mDigite um número inteiro: \033[m'))

print('\n\033[46mEscolha uma das bases para conversão:\033[m\n')
print('\033[33m[1] para converter para BINÁRIO\033[m')
print('\033[34m[2] para converter para OCTAL\033[m')
print('\033[35m[3] para converter para HEXADECIMAL\n\033[m')

option=int(input('\033[42mSua opção: \033[m'))

if option==1:
    print('\033[33m\nO número {}, em Binário é: {}\033[m\n'.format(n1, bin(n1)[2:]))
elif option==2:
    print('\033[34m\nO número {}, em Octal é: {}\033[m\n'.format(n1, oct(n1)[2:]))
elif option==3:
    print('\033[35m\nO número {}, em Hexadecimal é: {}\033[m\n'.format(n1, hex(n1)[2:]))
else:
    print('')
    print('\033[41mEsta não é uma opção válida!\033[m\n')
