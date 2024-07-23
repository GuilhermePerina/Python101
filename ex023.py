import math

n=float(input('Qual é o ângulo? '))
n1=math.sin(n)
n2=math.cos(n)
n3=math.tan(n)

print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(n1, n2, n3))
