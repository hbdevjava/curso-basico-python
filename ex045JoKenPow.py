from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUA OPÇOES
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é a sua Jogada??'))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('Pow')
sleep(1)
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Ganhouu')
    elif jogador == 2:
        print('Compurador Ganhou')
    else:
        print('INVALIDO')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('Compurador Ganhou')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Ganhou')
    else:
        print('INVALIDO')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('Jogador Ganhou')
    elif jogador == 1:
        print('Compurador Ganhou')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('INVALIDO')