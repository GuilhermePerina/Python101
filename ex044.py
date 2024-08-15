# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou ntão o emprestimo será negado.

print('==='*20)
print('\033[7;40mvamos simular o seu empréstimo!\033[m')

valor=float(input('\033[32mQual o valor da casa que você quer financiar? \033[m'))
salario=float(input('\033[33mQual o seu salário? R$ \033[m'))
tempo=int(input('\033[34mEm quantos anos você pretende pagar o imóvel? \033[m'))

parcela=valor/(tempo*12)

print('Para pagar um imóvel de {:.2f}, em {} anos, o valor da sua parcela mensal seria de R$ {:.2f}'.format(valor, tempo, parcela))

if parcela<=0.3*salario:
    print('\033[42mParabéns, seu imóvel próprio está a caminho, pois o seu emprestimo foi concedido!\033[m')
else:
    print('\033[41mPorém, nós sentimos muito, mas seu empréstimo foi negado!\033[m')
