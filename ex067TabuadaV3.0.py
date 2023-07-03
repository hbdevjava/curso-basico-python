while True:
    n = int(input('Digite um numero para ver a tabuada: '))
    if n <= 0:
        break

    print('-' * 30)
    for c in range(1, 11):
         print(f'{n} x {c :2} = {n*c}') #{:2} é usado pra alinhar as linhas da Tabuada
    print('-' * 30)
print('PROGRAMA Tabuada ENCERRADA')
print('-=-' * 20)
print('{:=^60}'.format(' HB '))

while True:# o break esta atrelado ao 'while True:'
    num = int(input('Digite um numero para ver a tabuada: '))
    if num <= 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c :2} = {num*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADA')