numeros = list()
while True:
    n = int(input('Digite um Valor...'))
    if n not in numeros:
        numeros.append(n)
        print('Numero add com sucesso...')
    else:
        print('Valor Duplicado...')
    r = ' '
    while r not in 'SN':
        r = str(input('Quer Continuar??? [S/N]?')).strip().upper()[0]
    if r == 'N':
        break
numeros.sort()
print(f'Voce Digitou os Valores {numeros}')

print('Acabou...')

''' r = ' '
    while r not in 'SN':
        r = str(input('Quer Continuar??? [S/N]?')).strip().upper()[0]
    if r == 'N':
        break 
        ESSE COD ME GARANTE A VALIDAÇAO DO SIM E DO NAO '''