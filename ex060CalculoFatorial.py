print('**** USANDO O MODULO MATH ****')
from math import factorial
num = int(input('Digite um numero: '))
f = factorial(num)
print('Factorial de {} e {:.0f}'.format(num, f))


print('-=-' * 30)
print('**** USANDO O WHILE ****')
from math import factorial
num = int(input('Digite um numero: '))
c = num
f = factorial(num)
print(' Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(', ' if c > 1 else '=', end=' ') # da opra colocar um if dentro do print
    # SE O C FOR MAIOR QUE 1 COLOQUE ',' SE NAO COLOQUE '='
    c -= 1
print('{}'.format(f))
print('-=-' * 30)
print('**** USANDO O FOR ****')

n = int(input('Digite um numero: '))
f = 1
for c in range(1, n, 1):
    f *= n
    n -= 1
print('O fatorial é {}'.format(f))

''' O NUMERO FATORIAL SEMPRE COMEÇA COMEÇA COM 1'''

'''n = int(input('Digite um numero: ')) ==> O NUMERO QUE DESEJA O FATORIAL (5)
f = 1 ==> FATORIAL SEMPRE COMEÇA COM 1 
for c in range(1, n, 1): ==> INICIO 1, ATE O NUMERO DIGITADO, INDO DE 1 EM 1 EX: 1, 2, 3, 4, 5
    f *= n ==> FATORIAL = ELE MESMO X O MUMERO DIGITADO
    n -= 1 ==> DO NUMERO DIGITADO AO 1 DE 1 - 1 EX:5-1=4, 4-1=3, 3-1=2, 2-1=1
print('O fatorial é {}'.format(f))'''