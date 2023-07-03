'''print('**** USANDO O FOR ****')
primeiro = int(input('Primeiro TERMO: '))# O NUMERO DE INICIO
razao = int(input('RAZAO: '))# DE UM EM UM OU DOIS EM DOIS ...
decimo = primeiro + (10 - 1) * razao
for contador in range(primeiro, decimo + razao, razao):
    print('{} '.format(contador), end='-> ')
print('ACABOU')

print('-=-' * 30)
a = int(input('Primeiro TERMO: '))# O NUMERO DE INICIO
b = int(input('RAZAO: '))# DE UM EM UM OU DOIS EM DOIS ...
c = a
print('{} -> '.format(a), end=' ')
while a != c + 9*b:
    a += b
    print('{} -> '.format(a), end=' ')
print('FIM')'''

print('-=-' * 30)
print('**** USANDO O WHILE ****')
print('GERADOR DE PA')
p = int(input('Primeiro TERMO: '))# O NUMERO DE INICIO
r = int(input('RAZAO: '))# DE UM EM UM OU DOIS EM DOIS ...
termo = p
cont = 1
while cont < 10:
    print('{} -> '.format(termo), end=' ')
    termo = termo + r
    cont += 1
print('FIM')
