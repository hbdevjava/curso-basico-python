soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {}º valor: '.format(c)))
    if num % 2 == 0: # c % 3 == 0: (IMPAR) c % 2 == 0:(PAR)
        soma += num  # acumulador normalmente soma um valor
        cont += 1  # contador normalmente soma +1
print('Voce informou {} numeros PARES e a soma total foi {}'.format(cont, soma))