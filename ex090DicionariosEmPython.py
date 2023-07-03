aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A media do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperaçao'
else:
    aluno['situacao'] = 'Reprovado com Louvor'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
    print()