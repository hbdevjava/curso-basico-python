nome = input('Qual seu nome?')
print('\033[7;30m prazer em te conhecer, {:=^20}!!\033[m'.format(nome))

n1 = int(input('um Valor: '))
n2 = int(input('outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end='')
print('Divisao inteira {}, e potencia {}...'.format(di, e))



