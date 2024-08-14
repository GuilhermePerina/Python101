
print('\033[41mPreste bastante atenção no exercício abaixo!!\033[m')

posicao=str(input('Qual bebida você gostaria de tomar nesta noite maravilhosa? (escolha entre "caipirinha", "mojito" ou "cuba libre"): '))

if posicao==str('caipirinha'):
    print('Huuummm, essa bebida Brasileira é interessantíssima!')
elif posicao==str('mojito'):
    print('Eu ouvi dizer que a maioria das pessoas gostam dessa bebida!')
elif posicao==str('cuba libre'):
    print('Excelente escolha, eu adoro essa bebida!')
else:
    print('Desculpe, não temos essa bebida em nosso cardápio')
