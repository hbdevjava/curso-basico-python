frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A apareceu {}x na frase.'.format(frase.count('a')))# count(' ')conta quantas x tem algo na frase
print('A primeira letra A apareceu na posiçao {}.'.format(frase.find('a')+ 1))
print('A ultima letra A apareceu na posiçao {}.'.format(frase.rfind('a')+ 1))


