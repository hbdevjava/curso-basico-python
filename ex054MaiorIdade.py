from datetime import date
dataAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ana a {}º paeeos nasceu? '.format(pessoa)))
    idade = dataAtual - nascimento
    if idade >= 21:
        totalMenor += 1
    else:
        totalMaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totalMenor))
