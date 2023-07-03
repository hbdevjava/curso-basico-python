somaIdade = 0
mediaIdade = 0
maiorIdadeH = 0
nomeDoMaisVelho = ''
totalMulher20 = 0
for p in range(1, 5):
    print('------ {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':# sexo in 'Mm' MAIOR E MENOR
        maiorIdadeH = idade
        nomeDoMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeH:
            maiorIdadeH = idade
            nomeDoMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
                totalMulher20 += 1

mediaIdade = somaIdade / 4
print('A media de idade do grupo é de {} anos '.format(mediaIdade))
print('O homem mais velho tem {} anos'.format(maiorIdadeH))
print('O nome do homem mais velho é {}'.format(nomeDoMaisVelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totalMulher20))
