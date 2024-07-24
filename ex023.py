import math

n=float(input('Qual é o ângulo? '))
n1=math.sin(math.radians(n))
n2=math.cos(math.radians(n))
n3=math.tan(math.radians(n))

print('O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(n1, n2, n3))
