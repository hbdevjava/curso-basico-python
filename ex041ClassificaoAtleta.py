from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Qual o ano de Nascimendo do Atleta?.. '))
idade = anoAtual - anoNascimento
print('O Atleta tem {} anos de idade...'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM ')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL ')
elif idade <= 19:
    print('Categoria: JUNIOR ')
elif idade <= 25:
    print('Categoria: SENIOR ')
else:
    print('MASTER')



