from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?? '))# O Jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens vc conseguiu me vencer')
else:
    print('EU Ganhei... eu pensei no numero {} e vc escolheu {}'.format(computador, jogador))




