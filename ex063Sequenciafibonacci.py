'''print('--'*30)
print('SEQUENCIA DE FIBONACCI')
print('--'*30)
n = int(input('Quantos TERMOS voce deseja mostrar? '))
t1 = 0
t2 = 1
print('--'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')'''

print('--'*50)
valor = int(input('Quantos termos vc deseja mostar? '))
termo1 = 0
termo2 = 1
print('{} -> {}'.format(termo1, termo2), end='')
contador = 3
while contador <= valor:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' -> FIM')
