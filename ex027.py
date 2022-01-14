nome = input('Digite seu nome completo: ').strip().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0].capitalize()}')
print(f'Seu último nome é {nome[-1].capitalize()}')
print(f'Seu último nome é {nome[len(nome)-1].capitalize()}')


"""nome = str(input('Qual é o seu nome? ')).strip()
a = nome.find(' ')
b = nome.rfind(' ')
print('o seu primeiro nome é: {}'.format(nome[:a]))
print('o seu último nome é: {}'.format(nome[b+1:]))"""