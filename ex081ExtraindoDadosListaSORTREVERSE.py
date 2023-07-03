valores = []
while True:
        valores.append(int(input('Digite um Valor: ')))
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if resposta in 'Nn':
           break
print('-=-'* 30)
print(f'Foram digitados {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Elementos em ordem Decrescente: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da Lista')
else:
    print('O valor 5 nao faz parte lista')