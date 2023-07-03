num = int(input('Informe o numero: '))
u = num // 1 % 10 # divisao inteira por 1,(modulo) resto da divisao
d = num // 10 % 10 # divisao inteira por 10,(modulo) resto da divisao
c = num // 100 % 10 # divisao inteira por 100,(modulo) resto da divisao
m = num // 1000 % 10 # divisao inteira por 1000,(modulo) resto da divisao
print('Analizando o numero {}'.format(num))
print('unidade:{}'. format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))
