# Alistamento Militar
from datetime import  date
anoAtual = date.today().year
nascimento = int(input('Digite o ano em que voce nasceu: '))
idade = anoAtual - nascimento
print('Quem nascem em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento...'.format(saldo))
    ano = anoAtual + saldo
    print('Que sera no ano de  {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria tem se alistado ha {} anos.'.format(saldo))
    ano = anoAtual - saldo
    print('No ano de {}'.format(ano))

