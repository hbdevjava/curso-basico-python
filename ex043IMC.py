peso = float(input('Digite o Peso: '))
altura = float(input('Digite a Altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do Peso ')
elif 18.5 <= imc < 25:
    print('Peso IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA...')
