jogador = dict() #DISCIONARIO
partida = list() #LISTA
jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
for c in range(0, total):
    partida.append(int(input(f'Quantidade de gols na {c+1}º partida foi ? ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas ')
#ele pode pegar a quantidade de partidas {len(jogador["glos"]) pq a quantidade de gols esta dividido por partidas
for i, v in enumerate(jogador['gols']):
    print(f'   => Na {i+1}º Partida ele fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
