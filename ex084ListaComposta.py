temp = list()
principal = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: '))) # TEMP[0]
    temp.append(float(input('Peso: '))) #TEMP[1]
    if len(principal) == 0: # SE NAO CADASTREI NINGUEM AINDA, ENTAO
        maior = menor = temp[1] # O MAIOR É IGUAL O MENOR QUE É IGUAL A TEMP NA POSIÇAO [1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('-=-'*30)
print(f'Os Dados Obtidos foram {principal}')
print(f'O maior peso encontrado foi de {maior}kg', end='')
for p in principal:
    if p[1] == maior:
        print(f' e {p[0]} é o mais pesado(a)')

print(f'O menor peso encontrado foi de {menor}kg', end='')
for p in principal:
    if p[1] == menor:
        print(f' e {p[0]} é o mais leve de todos')