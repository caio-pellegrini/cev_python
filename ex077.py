palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro', 'pneumoultramicroscopicossilicovulcanoconiótico')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos ', end='')
    for vogal in palavra:
        if vogal in 'aeiou':
            print(vogal, end=' ')
    print()
