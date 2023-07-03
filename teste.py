'''entrada = input('Digite [E]ntrar or [S]air: ')
senha_digitada = input('Digite sua senha: ')
senha_permitida = '1234'

if (entrada == 'e' or entrada == 'E') and senha_digitada == senha_permitida:
        print('Acesso Permitido')
else:
        print('Acesso NEGADO')'''
from builtins import print

'''hora_certa = int(input('Que horas sao?: '))

if 0 < hora_certa <= 11:
    print('BOM DIA!!!!')
elif 12 <= hora_certa < 17:
    print('BOA TARDE!!!')
elif 18 <= hora_certa <= 22:
    print('Boa Noite!!!')
else:
    print('...')'''
'''nome = input('Digite seu nome: ')
nome_tamanho = len(nome)

if nome_tamanho <= 1:
    if nome_tamanho <= 4:
        print('Seu nome é curto')
    elif nome_tamanho >= 5 and nome_tamanho <=6:
        print('Seu nome é normal')
    elif nome_tamanho > 6:
        print('eu nome é muito grande')
    else:
         print('Digite pelo menos uma letra')'''


print('{:=^60}'.format(' Calculadora com while '))
while True:
    num_1 = input('Digite o primeiro numero: ')
    operador = input('Escolha um operador [+-*/]: ')
    while operador not in '+-*/':
        print('Operador Invalido')
        operador = str(input('Escolha um operador [+-*/]: '))

    num_2 = input('Digite o segundo numero: ')

    numero_1 = 0
    numero_2 = 0
    numero_validos = None

    try:
        numero_1 = float(num_1)
        numero_2 = float(num_2)
        numero_validos = True

        ...
    except:
        numero_validos = None
        print('Digite algo valido...')
        continue

    # print('Seu Resultado sera apresentado a baixo...')
    if operador == '+':
        print(f'O Resultado de {numero_1:.0f} + {numero_2:.0f} =', numero_1 + numero_2)
    elif operador == '-':
        print(f'O Resultado de {numero_1:.0f} - {numero_2:.0f} =', numero_1 - numero_2)
    elif operador == '*':
        print(f'O Resultado de {numero_1:.0f} * {numero_2:.0f} =', numero_1 * numero_2)
    elif operador == '/':
        print(f'O Resultado de {numero_1:.0f} / {numero_2:.0f} =', numero_1 / numero_2)
    else:
        print('Valor invalidos...')
    sair = str(input('Quer sair do programa [S/N]:')).upper().startswith('S')
    if sair is True:
        break
print('Obrigado e Volte Sempre!!!!')

'''start = 0
end = 10
while start < end:
    print(start)
    start += 1'''


'''print('{:=^60}'.format(' Jogo Palavra Secreta. '))
palavra_secreta = 'hebert'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1: # se to tamanho digitado for maior do que 1
        print('Digite apenas uma letra.') # print('Digite apenas uma letra.')
        continue # volta pra letra_digitada = input('Digite uma letra: ')

    if letra_digitada in palavra_secreta:# se a letra digita for uma das que tem na palavra_secreta
        letras_acertadas += letra_digitada # entao letras_digitadas salva em letras_acertadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta: # se letra_secreta tiver em palavra_secreta
        if letra_secreta in letras_acertadas:# se letra_secreta for algumas das salvas em letras_acertadas
            palavra_formada += letra_secreta # entao palavra_formado recebe ela mesmo + letra_secreta

        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        # os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0'''

print('{:=^60}'.format(' Jogo Palavra Secreta. '))
palavra_secreta = 'hebert'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra...')

    if len(letra_digitada) > 1:
        print('Digite apanas uma Letra...')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas = letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')
