valor = int(input('Entre com um número para saber a tabuada: '))
aux = 0
print('-'* 10)
print('Tabuada de {}'.format(valor))
while(aux <= 10):
  print('{} X {} = {}'.format(aux, valor, (aux * valor)))
  aux = aux + 1
print('-' * 10)
