from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opçao = 0
while opçao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS 
    
    [5] SAIR DO PROGRAMA''')
    opçao = int(input('Qual a sua OPÇAO?'))
    if opçao == 1:
        soma = n1 + n2
        sleep(1)
        print('A soma entre {} e {} é de {}'.format(n1, n2, soma))
    elif opçao == 2:
        multiplicaçao = n1 * n2
        sleep(1)
        print('A multiplicaçao entre {} e {} é de {}'.format(n1, n2, multiplicaçao))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            sleep(1)
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os numeros Novamente:')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opçao == 5:
        sleep(1)
        print('FINALIZANDO...')
    else:
        print('Opçao Invalida Tente Novamente...')
    print('-=-' * 40)
    sleep(1)
print('FIM do PROGRAMA')

