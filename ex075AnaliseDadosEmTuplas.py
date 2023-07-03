num = (int(input('Digite um numero...')),
       int(input('Digite um numero...')),
       int(input('Digite um numero...')),
       int(input('Digite um numero...')))
print(f'Voce digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3) + 1}ª posiçao')# sempre que buscar a posicao lembrar que acrencentar {num.index(3) + 1}
else:
    print('O valor 3 nao foi digitado...')
print('Os valores Pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')