listaNum = []
maior = menor = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um Valor para a posiçao {c}: ')))# esse cod da a posiçao de 0 a 4
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior: # esse cod mostra o maior e menor na sua respectiva posiçao
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c]
print('-=-' * 30)
print(f'Voce digitou os valores {listaNum}')
print(f'O maior Valor digitado foi {maior} na posiçao ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'...{i}', end='')
print(f'\nO menor valor digitado foi {menor} na posiçao ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'...{i}', end='')
print()
