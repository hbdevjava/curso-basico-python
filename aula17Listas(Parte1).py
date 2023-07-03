#num = ['hotdog', 'hamburg', 'suco', 'pizza', 'pudim']
#num[1] = 3 (isso nao pode ser feito)
#print(num)
#num.sort(reverse=True)# mostra a lista de tras pra frente (DECRESCENTE)
#num.sort() # mostra a lista em ordem alfabetica
#print(num)
#num.append(6)
#print(num)
#num.insert(2, 0) #NA POSIÇAO 2 INSIRA O NUMERO ZERO
#print(num)
#num.pop(2)
#del num[3]
#num.remove(3)
#print(num)
'''if 'suco' in num: #O OPERADOR 'IN' É PODEROSO PRA VARIAVEIS COMPOSTAS NO PYTHON
    num.remove('suco')
print(num)'''
'''valores = list(range(4, 11))
print(valores)'''
#print(f'Essa lista tem {len(num)} elementos')
#print(num)
#num.insert(1, 'sopa')
#num.insert(0, 'carne')
'''if 'suco' and 'hamburg' and 'pudim' and 'pizza' in num:
    num.remove('suco')
    num.remove('hamburg')
    num.remove('pudim')
    num.remove('pizza')
        if 'pizza' in num:
            num.remove('pizza')
                 if 'pudim' in num:
                    num.remove('pudim')
else:
    print('element is not found, try it again')
#print(f'Essa lista tem {len(num)} elementos')
print(num)'''
almoço = []
almoço.append('arroz')
almoço.append('feijao')
almoço.append('batata frita')
almoço.append('carne')
print(almoço)
for co in almoço:
    print(f'Hoje vou almoçar {co}')
print('-+-'*30)
for c, co in enumerate(almoço):
    print(f'na {c}ª posiçao, Hoje vou almoçar {co}')
print('-+-' * 30)
'''for cont in range(0, 4):
    almoço.append(str(input('Quer comer o que ???   ')))'''
print('-+-' * 30)
a = [2, 3, 4, 7]# b = a => QUANDO FAÇO ISSO EU ESTOU CRIANDO UMA LIGAÇAO ENTRE AS LISTAS O QUE MUDA NUMA MUDA NA OUTRA
b = a[:]# aqui eu crio uma copia e posso alterar cada uma separadamente b[2] = 8 b nao tem mais ligaçao com a
b[2] = 8
print(f'Lista A...{a}')
print(f'Lista B...{b}')