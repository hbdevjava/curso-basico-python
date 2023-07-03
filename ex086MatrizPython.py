matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''        0  1  2    0  1  2    0  1  2
              0          1          2    '''
for l in range(0, 3): #linha
    for c in range(0, 3): #coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()