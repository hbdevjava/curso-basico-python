totaValor = totalmil = menor = cont = barato = maisCaro = 0
while True:
    produto = str(input('NOME do Produto: '))
    preço = float(input('PREÇO do Produto: '))
    cont += 1
    totaValor += preço
    if preço >= 1000:
        totalmil += 1
        maisCaro = produto
        maiorValor = preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    else:
        if preço < menor:
           menor = preço
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer CONTINUar[S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total da compra foi de R$:{totaValor:.2f}')
print(f'Temos {totalmil} produdos custando + de MIL REAIS que é o {maisCaro} no valor de R$:{maiorValor}')
print(f'O produto mais barato foi {barato} que custa R$:{menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA'))

'''menor = cont = 0
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
           menor = preço 
esse cod me mostra o valor mais barato dentre os produtos registradosk'''

