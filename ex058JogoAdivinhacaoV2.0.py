from random import randint

computador = randint(0, 10)# Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10, tente adivinhar...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em que numero eu pensei?? '))  # O Jogador tenta adivinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...')
        elif jogador > computador:
            print('MENOS...')
print('ACERTOU... apos {} Tentativas'.format(palpites))
print('-=-' * 20)

