'''from random import randint
from time import sleep
vitoria = 0
while True:
    jogador = int(input('Escolha um valor: '))
    sleep(1)
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OR IMPAR? [P/I]: ')).strip().upper()[0]# strip()tira espaços do começo e final da string
    print(f'Voce jogou {jogador} e o computador jogou {computador}. (No total de {total}),', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')# estruturas condicionais dentro de um print
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc Venceu!!!')
            vitoria += 1
        else:
            print('Voce PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vc Venceu!!!')
            vitoria += 1
        else:
            print('Voce PERDEU!!!')
            break
    print('Voce joga novamente...')
print(f'GAME OVER: vc venceu {vitoria} vezes')'''
print('-=-' * 20)
print('{:=^60}'.format(' HB '))

from random import randint
from time import sleep
vitoria = 0
while True:
    jogador = int(input('Qual numero vai jogar? '))
    sleep(1)
    compurador = randint(0, 10)
    total = jogador + compurador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OR IMPAR [P/I]? ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o Computador jogou {compurador}. no total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!!!')
            vitoria += 1
        else:
            print('VOCE PERDEU!!!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!!!')
            vitoria += 1
        else:
            print('VOCE PERDEU!!!')
            break
    print('VAMOS JOGAR NOVAMENTE....')
print(f'GAME OVER...Voce perdeu {vitoria} vezes')