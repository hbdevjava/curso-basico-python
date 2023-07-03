num = cont = soma = 0
while True:
    num = int(input('DIGITE UM NUMERO [999 PARA PARAR]: '))  # [999] FLAG
    if num == 999:
        break #INTERROMPE O FLUXO DO LAÇO
    soma += num # soma = soma + num
    cont += 1 # cont = cont + 1
print(f'Voce digitou {cont} numeros e a soma foi {soma} ')# Interpolação

print('-=-' * 20)
print('{:=^60}'.format(' HB '))
num = soma = cont = 0
while True: # como preciso usar o comando break, uso o true pra usar o comando break dentro do laço
    num = int(input('Digite um valor: ')) # o break esta atrelado ao 'while True:'
    if num == 999:
        break # ele sai do laço e nao adciona o [999] na somatoria dos valores
    soma += num
    cont += 1
print(f'Foram digitados {cont} numeros e a soma deles é {soma}')

#python nao exige declaraçao de variaveis

