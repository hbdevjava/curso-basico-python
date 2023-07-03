#TUPLAS SAO IMUTAVEIS
times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence',
        'Atletico', 'BotaFogo', 'Atlatico-PR', 'Bahia'
        'Sao Paulo', 'Fluminense', 'Sport Recife',
        'Ec Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
        'Atletico-GO')
print('-=-'* 60)
print(f'LISTA DE TIMES: {times}')
print('-=-'* 60)
print(f'Os Primeiros Colocados sao {times[0:5]}')
print('-=-'* 60)
print(f'Os Ultimos 4 Colocados sao {times[-4:]}')
print('-=-'* 60)
print(f'Times em Ordem Alfabetica {sorted(times)}')# Ordem ALFABETICA
print('-=-'* 60)
print(f'Chapecoence está na POSICAO [{times.index("Chapecoence")+1}]')#como ja tem aspas simples de fora se tem que usar aspas duplas