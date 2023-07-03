lanche = 'Hamburg', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[0:3])
print(lanche[:2])
print(lanche[-3:])
#Tupla sao Imutaveis
print(lanche)
'''lanche[1] = 'Biscoito'
print(lanche)
 Traceback (most recent call last):
  PycharmProjects\pythonProject\pythonexercicios\aula16Tuplas.py", line 11, in <module>
    lanche[1] = 'Biscoito'
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
O python me devolve um TRACEBACK dizendo que o objeto em questao nao pode ser modificado ou seja 
nao pode ter itens atribuidos'''
print('-=-'*30)
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim', 'Refri'
print(len(lanche))
for c in range(0, len(lanche)):
    print(c)
# ***************************************************************************
print('-=-'*30)
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim', 'Refri'
for c in range(0, len(lanche)):
    print(lanche[c])
print('-=-'*30)
# USANDO O FOR NO RANGE
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim', 'Refri'
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
print('Aff vou comer demais')
print('-=-'*30)
# USANDO O FOR DIRETAMENTE NA VARIAVEL LANCHE (mais simples se nao precisar de posiçao)
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Aff vou comer demais ')
print('-=-'*30)
# USANDO O ENUMERATE
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim', 'Refri'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}, na posiçao {pos}')
print('Aff vou comer demais ')
print('-=-'*30)
# *****************************************************************
lanche = 'Hambung', 'Suco', 'Pizza', 'Pudim', 'Refri'
print(sorted(lanche)) # MOSTRA EM ORDEM ALFABETICA
print('-=-'*30)
# ************************************************************
a = 2, 5, 4
b = 5, 8, 1, 2
print(a + b)
print('-=-'*30)
# *****************************************************
a = 2, 5, 4
b = 5, 8, 1, 2
print(b + a)
print('-=-'*30)
# *****************************************************
a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c)
print(c.count(2)) # quantas vezes aparece o numero 2
print(c.index(8)) # em qual posiçao esta o numero 8
print(c.index(5, 1))# o 5 a partir da posiçao 1 (como ja tem um 5 na posiçao 0 ele nao conta)
print('-=-'*30)
# ************************************************
pessoa = 'HB', 33, 'Masculino', 6.858
print(pessoa)