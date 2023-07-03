# CONSEGUI FINALIZAR SOZINHO AMEM SENHOR
cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis',
        'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
        'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0<= num <= 20:
                break

        print('tente novamente...', end='')
print(f'Voce digitou a numero {cont[num]}')
resposta = ''
while True:
        resposta = str(input('Quer continuar [S/N]?')).strip().upper()[0]
        if resposta == 'S':
                while True:
                        num = int(input('Digite um numero entre 0 e 20: '))
                        if 0 <= num <= 20:
                                break

                        print('tente novamente...', end='')
                print(f'Voce digitou a numero {cont[num]}')
        if resposta == 'N':
                break
print('FIM do Programa!!!!')