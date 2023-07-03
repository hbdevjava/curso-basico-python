preço = float(input('Qual o preço do produto?'))
novo_preço = preço - (preço*25/100)
print('O preço do produto é {:.2f}, com desconto de 25% fica {:.2f}'.format(preço, novo_preço))

