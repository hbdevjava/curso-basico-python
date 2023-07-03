from builtins import print

frase = 'Hebert de Souza Brito'
print(frase.upper(), '| ''Upper')
print(frase.lower(), '| ''Lower')
print(frase.capitalize(), '|'' Capitalize')
print(frase.title(),'|'' Title')
print('-' * 30)
print('Quantas letras tem o primeiro nome?')
print(frase)
print(len(frase[:5]))
print('souza'.capitalize() in frase)
print(frase.find('Brito'))
print('-' * 30)
print('Quantas letras sem considerar os espaços?')
print('*' * 30)
print('*' * 30)
nome = str(input('Qual o seu nome?')).strip()
print('Analizando seu nome....')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minuscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # nome.count == contador de espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))





