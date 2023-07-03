total18 = totalH = totalF = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '#tem que começar vazio pra validar o [M/F]
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'f' and idade < 20:
        totalF += 1
    resposta = ' '#tem que começar vazio pra validar o [S/N]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessaos com mais de 18 anos sao {total18} pessoasii, ')
print(f'Ao todo temos {total18} homens cadastrados')
print(f'Temos {totalF} mulheres com menos de 20 anos')
'''
    if idade >= 18:
        total18 += 1
    esse cod me msotra quantas pessoas tem mais de 18 anos... ele varre o programa e mostra 
    quantos pessoa sao maiores de 18 anos
    OUTROS EXEMPLOS:
     if sexo == 'M':  
        totalH += 1 
    if sexo == 'f' and idade < 20:
        totalF += 1 
'''