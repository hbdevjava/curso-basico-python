# Condiçao Simples
velocidade = float(input('Qual a velocidade atual do seu carro??'))
if velocidade > 80:
    print('MULTADO!! vc ultrapassou a velocidade maxima permitido de 80km/h')
    multa = (velocidade - 80) * 7
    print('Vc deve pagar uma multa de R${:.2f}!=888'.format(multa))
print('Siga com cuidade!!!')
