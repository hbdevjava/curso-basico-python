from builtins import print

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('Sua opçao: '))
if opçao == 1:
    print('{} convertido para BINARIO é igual a {} '.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('INVALIDO')
