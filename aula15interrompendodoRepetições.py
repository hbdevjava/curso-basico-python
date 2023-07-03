cont = 1
while cont <= 10:
    print(cont, '--> ', end='')
    cont += 1
print(' FIM')
print('-=-'* 50)
'''O comando Break quebra um loop que esta sendo executado em uma sequencia de vezes'''
# LIMITANDO O WHILE
n = cont = 0
while cont < 3:# ==> aqui vc limita o laço a 5 iteracoes
    n = int(input('DIGITE UM NUMERO: '))
    cont += 1
print('FIM')

print('-=-' * 50)
n = soma = 0
while n != 999:# ==> flag
    n = int(input('DIGITE UM NUMERO: '))
    soma += n
print('A soma vale {}'.format(soma - 999))
print('-=-' * 50)
# USANDO O BREAK
n = soma = 0
while True:
    n = int(input('DIGITE UM NUMERO: '))
    if n == 999:
        break
    soma += n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}') # F strings usa a interpolaçao
# Usando o BREAK nao precisa dessa ganbiarra ==> print('A soma vale {}'.format(soma - 999))
print('-=-' * 50)
nome = 'HB'
idade = 33
print(f'O {nome} tem {idade} anos') #PYTHON 3.6+