from builtins import print

time = list() #Lista
jogador = dict() #DISCIONARIO
partida = list() #LISTA
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
    partida.clear()
    for c in range(0, total):
        partida.append(int(input(f'Quantidade de gols na {c+1}º partida foi ? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar?? [S/N]? ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO: Digite apenas S ou N')
    if resposta == 'N':
        break

print('-=' * 40)                 # LINHA 23/27 ESSE COD CRIA UM CABEÇALHO
print(' COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')# 3 caracters centralizado a direita
    for d in v.values():
        print(f'{str(d):<15}', end='')#:<15 carateres alinhado a direita
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):#AQUI GARANTE NAO PASSAR UMA VALOR MAIOR QUE O TAMANHO DA LISTA (TIME)
        print(f'ERRO: Nao existe jogador com o codigo {busca}! ')
    else: # caso tenha algo dentro dos limites do (lista)(time)
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No {i+1}º jogo {time[busca]["nome"]} fez ({g}) gols')
    print('-='*40)
print('Volte Sempre')