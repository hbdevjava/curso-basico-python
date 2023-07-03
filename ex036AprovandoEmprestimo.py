casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Salario do Comprador: R$'))
financiamento = int(input('Em quantos anos de Financiamento??'))
prestaçao = casa / (financiamento * 12)
minimo = salario * 30 / 100 # Calculo de porcetagem
print('Para pagar uma casa de R$:{:.2f} em {} anos, a prestaçao sera de R$:{:.2f}'.format(casa, financiamento, prestaçao))
if prestaçao <= minimo: # O valor minimo pra ser aceito é 30% do salario
    print('EMPRESTIMO pode ser CONCEDIDO')
else:
    print('EMPRESTIMO foi NEGADO')
