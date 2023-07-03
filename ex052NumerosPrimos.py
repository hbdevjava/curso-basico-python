num =int(input('Digite o numero: '))# numero primo so é divivel por 1 e por ele mesmo...
tot = 0
for c in range(1, num + 1): # + 1 faz com que chege ao numero digitado
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end="")#  end="" deixa na mesma linha...
print('\n\033[mO numero {} foi divisivel {} vezes '.format(num, tot))
if tot == 2:
    print('É numero PRIMO!!!')
else:
    print('Nao é numero PRIMO')
