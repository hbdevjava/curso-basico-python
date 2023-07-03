print('-=-' * 30)
print('**** USANDO O WHILE ****')
print('GERADOR DE PA')
p = int(input('Primeiro TERMO: '))# O NUMERO DE INICIO
r = int(input('RAZAO: '))# DE UM EM UM OU DOIS EM DOIS ...
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos TERMOS vc quer mostrar a mais?:  '))
print('Progressao finalizada com {} TERMOS mostrados'.format(total))
print('FIM')