def mensagem(msg):
    print('-='* 30)
    print('{:=^60}'.format(msg))
    print('-='* 30)



mensagem(' hb banck ')
valor = int(input('Qual o valor que deseja sacar? R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=+='* 30)
print('Volte sempra ao Banco HB')
mensagem(' volte sempre ')