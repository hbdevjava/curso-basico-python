matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''        0  1  2    0  1  2    0  1  2
              0          1          2    '''
somapares = maior = somacoluna = 0
for l in range(0, 3): #linha
    for c in range(0, 3): #coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) #valores da matriz
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') # formato da matriz
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
print(f'A soma dos numeros pares sao: {somapares}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somacoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da Segunda coluna é {maior}')
