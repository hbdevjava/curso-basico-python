#CONDIÇAO COMPOSTA

distancia = float(input('Qual a distancia da sua viagem?'))
print('Vc vai fazer um percuso de {:.0f}km'.format(distancia))
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 #SIMPLIFICADO
print('O preço da sua passagem sera de R${:.2f}'.format(preço))

