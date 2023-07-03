# Estrutura Condicional Aninhada!!!!
import emoji
nome = str(input('qual é o seu nome?'))
if nome == 'hebert':
    print('Nome lindo')
elif nome == 'maria' or nome == 'pedro' or nome == 'joao':
    print('Seu nome é bem popular'.format(nome))
elif nome in 'ana claudia julia ':
    print('belo nome feminino')
else:
    print(emoji.emojize('nome feio :smile:', language='alias'))
print('tenha um bom dia, {}!!'.format(nome))
