for c in range(10, 0, -1):
    print(c, end= ' ')
print('fim')

print('-=-' * 30)

i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c, end= ' ')
print('fim')