from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Qual a data de nascimendo: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho [0 -> nao tem]: '))
if dados['ctps'] != 0: # SE DADOS FOR DIFERENTE DE ZERO
    dados['contrataçao'] = int(input('Ano da Contrataçao:'))
    dados['Salario'] = float(input('Salario R$: '))
    dados['Aposentadoria'] = dados['idade'] + (dados['contrataçao'] + 35) - datetime.now().year
print('-='*30)
for k, v in dados.items():
    print(f'   -> {k} = {v}')
