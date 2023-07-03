print('{:=^40}'.format(' HB Tecnology '))
preço = float(input('preço das compras R$: '))
print(''' FORMAS DE PAGAMENTO
[1] A VISTA DINHEIRO OU PIX
[2] A VISTA NO CARTÃO
[3] EM 2X NO CARTÃO
[4] EM 3X OU MAIS NO CARTÃO''')
opçao = int(input('Qual a opçao escolhida??'))
if opçao == 1:
    valor = preço - (preço * 10 / 100)
elif opçao == 2:
    valor = preço - (preço * 5 / 100)
elif opçao == 3:
    valor = preço
    parcela = valor / 2
    print('Sua compra sera Pacelada em 2x de R${:.1f} SEM JUROS'.format(parcela))
elif opçao == 4:
    valor = preço + (preço * 20 / 100)
    totalParcela = int(input('Sera em quantas Parcelas?'))
    parcela = valor / totalParcela
    print('Sua compra sera Pacelada em {}x de R${:.1f} COM JUROS'.format(totalParcela, parcela))
else:
    valor = preço
    print('OPÇAO INVALIDA')

print('Sua compra de R${:.1f} vai custar R${:.1f} no final '.format(preço, valor))



