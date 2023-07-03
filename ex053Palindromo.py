frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]'''
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('Nao é Palindromo!!')

