'''r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmemtos acima podem formar Triangulos')
else:
    print('Os Segimemtos acima NÃO podem formar Triangulos')'''
print('=*=' * 40)

r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmemtos acima podem formar Triangulo ',
          end='')  # PODE FORMAR TRIANGULO OU NAO PODE? SE PODE QUE TIPO DE TRIANGULO SERA FORMADO
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os Segimemtos acima NÃO podem formar Triangulos')
