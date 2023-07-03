numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um Valor: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if res in 'Nn':
        break
for v in numeros:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-+-'*30)
print(f'A lista completa é {numeros}')
print(f'A lista de Pares é {pares}')
print(f'A lista de Impares é {impares}')
