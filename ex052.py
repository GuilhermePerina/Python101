#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

preco=float(input('Valor total das compras: R$ '))

print('\nFORMAS DE PAGAMENTO\n[1] Dinheiro\n[2] Débito\n[3] Crédito até 2x\n[4] Crédito até 12x\n')

forma=int(input('Qual será a forma de pagamento? ' ))

if forma<=3:
    if forma==1: 
        pagamento='dinheiro'
        desc='você tem 10% de desconto'
        total=preco*0.9
    elif forma==2:
        pagamento='débito'
        desc='você tem 5% de desconto'
        total=preco*0.95
    elif forma==3:
        pagamento='crédito em até 2x'
        desc='você não tem desconto'
        total=preco
    print('Para pagamento em {} {}, portanto o total a pagar é de {}'.format(pagamento, desc, total))
elif forma==4:
    parcelas=int(input('Em quantas parcelas você quer pagar? '))
    if parcelas>12:
        print('Não é possível parcelar em mais do que 12x')
    elif parcelas<3:
        print('Você errou a forma de pagamento selecionada')
    else:
        valorParcela=preco*1.2/parcelas
        print('Para pagamento no crédito em {}x o total a pagar é de {}, sendo {} parcelas de {}'.format(parcelas, preco*1.2, parcelas, valorParcela))
else:
    print('Opção inválida!')
