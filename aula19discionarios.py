def separador():
    print('-='*30)


def chamada(txt):
    print(txt)



dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
#print(dados)
print(dados['nome'])
print(dados['idade'])
separador()
#ADICONAR MAIS UM ELEMENTO AO DICIONARIO
#NO DICIONARO O COMANDO APPEND NAO FUNCIONA
dados['sexo'] = 'Masculino'
chamada(dados)
#DELETAR DADOS DE UM DICIONARIO
del dados['idade']
chamada(dados)
separador()

filme = {'titulo': 'Star Wars',
         'ano': '1977',
         'Diretor': 'George Lucas'}
chamada(filme)
print(filme.values())#PEGA O VALOR DE CADA CHAVE
print(filme.keys())#PEGA A CHAVE DE CADA VALOR
print(filme.items())#PEGA CHAVE/VALOR

for k, v in filme.items():
    print(f'O {k} é {v}')
separador()
cine = dict()
locadora = list()
cine['filme1'] = {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
cine['filme2'] = {'titulo': 'Vingadores', 'ano': '2012', 'diretor': 'joss Whedon'}
cine['filme3'] = {'titulo': 'Matrix', 'ano': '1999', 'diretor': 'Wachowski'}
locadora.append(cine['filme1'])
locadora.append(cine['filme2'])
locadora.append(cine['filme3'])
print(locadora)
print(len(locadora))
print(locadora[0]['ano'])
print(locadora[1]['titulo'])
print(locadora[2]['diretor'])
separador()
pessoas = {'nome': 'hebert', 'sexo': 'masculino', 'idade': '33'}
print(pessoas['nome'])
print(pessoas['idade'], 'anos')
print(pessoas['sexo'])
print(f'O {pessoas["nome"]} é do sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos de idade')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())#RETORNA UMA LISTA COMPOSTA DE 3 TUPLAS
pessoas['nome'] = 'Alisson'
pessoas['peso'] = 79
for k, v in pessoas.items():
    pessoas['nome'] = 'Alisson'
    print(f'{k} = {v}')
separador()
for c in pessoas.keys():
    print(c)
separador()
for v in pessoas.values():
    print(v)
separador()
#CRIAR UM DICIONARIO DENTRO DE UMA LISTA
brasil = list()
estado = dict()
'''estado1 = {'uf': 'ceara', 'sigla': 'ce'}
estado2 = {'uf': 'sao paulo', 'sigla': 'sp'}
estado3 ={'uf': 'rio de janeiro', 'sigla': 'rj'}
estado4 ={'uf': 'rio grande de norte', 'sigla': 'rn'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
brasil.append(estado4)
print(brasil)
print(len(brasil))
print(brasil[0])
print(brasil[0]['sigla'])
print(brasil[3]['uf'])
print(brasil[1]['sigla'])
print(brasil[2]['uf'])'''
separador()

'''for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    for k, v in estado.items():
        print(f'A {k} é {v}')
        (esse foi meu teste) '''
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())#o medoto append nao funiona nos dicionarios somente o copy()
#print(brasil)
print(len(brasil))

for c in brasil:
     for k, v in c.items():
         print(f'O campo {k} tem valor {v}')