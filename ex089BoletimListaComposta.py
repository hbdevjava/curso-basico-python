from django.utils.autoreload import file_changed

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostra notas de Qual Aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO>>>>')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')



''' len(ficha) - 1: eu cadastrei o aluno '0, 1, 2' ele tem ser '0, 1, 2' no poser ser mais do de isso
  tem quer menor do que a qquantidade de aluno cadastrado -1 pq o primeiro aluno é '0' e o ultimo é 'N-1' '''