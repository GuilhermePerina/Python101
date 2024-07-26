cidade=input('Digite o nome da cidade onde você mora: \n')

começo=cidade.split()

print('A sua cidade começa com a palavra "Santo"? {}'.format('Santo'in(começo[0])))
