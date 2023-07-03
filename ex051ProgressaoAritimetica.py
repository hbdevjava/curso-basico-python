primeiro = int(input('Primeiro TERMO: '))# O NUMERO DE INICIO
razao = int(input('RAZAO: '))# DE UM EM UM OU DOIS EM DOIS ...
decimo = primeiro + (20 - 1) * razao
for contador in range(primeiro, decimo + razao, razao):
    print('{} '.format(contador), end='-> ')
print('ACABOU')
