pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO: digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
                break
        print('ERRO: digite apenas S ou N')
    if resposta == 'N':
                break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas ')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print('-='*30)
print('As mulheres Cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
        print()
print('-='*30)
print('Lista das pessoas que estao a cima da media')
for p in galera:
    if p['idade'] >= media:
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
            print()
print('<<<< ENCERRADO >>>>')