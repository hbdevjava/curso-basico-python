palavras = ('aprender', 'programar', 'Linguagem', 'Phyton',
            'Curso', 'Gratis', 'Estudar', 'Praticar',
            'Trabalhar', 'Mercado', 'Futuro')
for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
