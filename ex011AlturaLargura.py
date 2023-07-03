larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print(f'Sua parede te a dimensâo de {larg} x {alt} se sua area é de {area}m²')
tinta = area / 2
print(f'Para pinta a parede voce precisa de {tinta:.0f}L de tinta.')