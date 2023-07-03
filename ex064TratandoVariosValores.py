num = cont = soma = 0
while num != 999:
    num = int(input('DIGITE UM NUMERO [999 PARA PARAR]: '))  # [999] FLAG
    soma += num # soma = soma + num
    cont += 1 # cont = cont + 1
print('Voce digitou {} numeros e a soma foi {}! '.format(cont-1, soma-999))#GAMBIARRA MELHOR USAR BREAK

