'''co = float(input('Comprimento do Cateto Oposto?'))
ca =float(input('Comprimento do Cateto Adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))
print('-' * 50)'''
from math import hypot
co = float(input('Comprimento do Cateto Oposto?'))
ca =float(input('Comprimento do Cateto Adjacente'))
hi = hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))


