nome = str(input('Digite se nome completo: '))
print('Prazer em te conhecer!')
print('seu primeiro nome é {} '.format(nome[:6]))
print('Seu ultimo nome é {} '.format(nome[16:]))
print('-' * 30)
print('-' * 30)
n = str(input('Digite se nome completo: ')).strip()
nome = n.split()
print(nome)
print('seu primeiro nome é {} '.format(nome[0])) # pra mim o meu nome tem 4 index pro Python ten 3
print('Seu ultimo nome é {} '.format(nome[len(nome)-1]))

