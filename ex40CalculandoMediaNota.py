n1 = float(input('Digite a Primeira NOTA: '))
n2 = float(input('Digite a Segunda NOTA: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a media de aluno é {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('Aluno foi RECUPERAÇAO ')
elif media < 5:
    print('Aluno esta de REPROVADO')
else:
    print('Aluno APROVADO')

