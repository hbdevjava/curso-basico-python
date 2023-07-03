soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c # acumulador normalmente soma um valor
        cont += 1 # contador normalmente soma +1
print('A soma de todos os {} numeros solicitados é {}'.format(cont, soma))



