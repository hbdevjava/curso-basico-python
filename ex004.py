information = input('digite algo:')
print('O tipo primitivo é ', type(information))
print('tem algum espaço? ', information.isspace())
print('ele é numerico? ', information.isnumeric())
print('ele é alfabetico? ', information.isalpha())
print('ele é alfaNumerico? ', information.isalnum())
print('ta em maiusculo?', information.isupper())
print('ta em minusculo?', information.islower())
print('ta em Capitalizada?', information.istitle())  # em maiusculo e minusculo
