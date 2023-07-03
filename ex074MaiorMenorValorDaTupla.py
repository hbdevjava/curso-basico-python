'''from random import randint
sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10))
print(f'Os numeros Sorteados sao: ', end='')
for n in sort:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(sort)}')
print(f'O menor valor Sorteado foi {min(sort)}')'''

from random import randint
sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10))
print(f'Os numeros Sorteados sao: ', end='')
maior = 1
menor = 5
for n in sort:
    print(f'{n} ', end='')
    if n == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'\nO maior Valor é {maior} e o menor é {menor}')

print('-+-'*60)
from random import sample
lista = tuple(sample(range(10), 5))
print(f'OS valores sorteados foram {lista}')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor Sorteado foi {min(lista)}')


