# HB TENHA MUITA ATENÇAO NESSA AULA
''' if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso '''
# ESSA ESTRUTURA TROCA O MENOR PESO PELO MAIOR E VIRCE E VERSA

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª Pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg.'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
