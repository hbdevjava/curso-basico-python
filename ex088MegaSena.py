#SEM DEIXAR QUE OS NUMEROS SE REPITA
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=-'*30)
print('{:=^60}'.format(' JOGAR NA MEGA SENA '))
print('-=-'*30)
quantidade = int(input('Quantos Jogos voce quer Sortear????... '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-='*3, f' SORTEANDO {quantidade} jOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1)
print('BOA SORTE HB')





