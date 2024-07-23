from math import floor
n=float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, floor(n)))


n1=float(input('Digite outro número: '))
n2=n//1
print('O número {1} tem a parte inteira {0:.0f}'.format(n2, n1))
