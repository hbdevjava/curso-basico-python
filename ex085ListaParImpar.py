'''ex: Geek Univercity

nome = str(input('Qual seu nome???'))
idade = int(input('Qual a sua Idede??'))
print(f'Seja bem vindo {nome}')
print(f'O {nome} tem {idade} de idade', end= ' ')
print(f'pois nasceu em {2023 - idade}')'''

numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor= int(input(f'Digite o {c}º um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=-'*30)
print(f'A lista completa de numeros é:  {numeros} ')
print(f'Os valores pares sao {sorted(numeros[0])}')
print(f'Os valores impares sao {sorted(numeros[1])}')
print()

