for c in range(1, 11):
    print(c, end=' ')
print('FIM')

print('-=-' * 40)
'''vc ler assim: o contador começa com 1, 
enquanto o contador nao chegar a 10 ele soma +1 ate 10'''
c = 1
while c < 11:
    print(c, end=' ')
    c += 1
print('FIM')
''' o FOR serve SOMENTE quando vc sabe o limite ex:range(1, 11)
Já o WHILE serve tanto pra quando se conhece o limite 
como pra quando nao se sabe qual o limite'''
print('-=-' * 40)
for c in range(1, 4):
    n = int(input('Digite um valor: '))
print('FIM')
print('-=-' * 40)
n = 1
while n != 5:
    n = int(input('Digite o numero: '))
print('FIM')
print('-=-' * 40)
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite o numero: '))
    resposta = str(input('Quer Continuar? [S/N]')).upper()
print('FIM')
print('-=-' * 40)
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite o numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros PARES e {} numeros IMPARES '.format(par, impar))

