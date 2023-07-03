'''dados = list()
dados.append('Hb')
dados.append(33)
print(dados)
pessoas = list()
pessoas.append(dados[:])
dados[0] = 'Son'
dados[1] = 25
pessoas.append(dados[:])
dados[0]= 'fabia'
dados[1] = 55
pessoas.append(dados[:])
print(pessoas)
print(len(pessoas))
print('-=-'*30)
galera = [['Hb', 33], ['Dora', 2], ['Alguem', 16]]
print(galera)
print(galera[2][0])
print(galera[1][0])
print(galera[2][1])
print('-=-'*30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
print('-=-'*30)
galera = list()
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])# NUNCA ESQUECER DE COPIA A LISTA
    dados.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade...')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade...')
        menor += 1
print(f'Temos {maior} Maior de idade e {menor} Menor de idade ')
