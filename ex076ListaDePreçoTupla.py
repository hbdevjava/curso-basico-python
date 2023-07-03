listagem = ('Lapis', 1.76,
            'Borracha0', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.39,
            'Caneta', 5.45,
            'Livro', 59.99)
print('-=-'*15)
print(f'{"LISTA DE MATERIAL ESCOLAR":^40}')
print('-=-'*15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

print('-=-'*15)