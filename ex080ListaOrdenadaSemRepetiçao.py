'''numLista = []

for c in range(0, 5):
    numLista.append(int(input(f'Digite o {c}ª numero: ')))
numLista.sort()
print(f'Voce digitou os valores{numLista}')'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adiconado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista...')
                break
            pos += 1
print('-=-'*30)
print(f'Os valores digitados em ordem foram {lista}')
