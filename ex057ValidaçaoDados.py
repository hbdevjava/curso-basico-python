sexo = str(input('Informe seu SEXO: [M/F]')).strip().upper()[0]# fatiamento vai pegar somente a primeira letra
while sexo not in 'MF':
    sexo = sexo = str(input('Dados invalidos informe o sexo correto: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso'.format(sexo))
