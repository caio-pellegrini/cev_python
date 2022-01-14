nome = input('Digite seu nome completo: ')
nome = nome.strip()
print(f'Seu nome é {nome.title()}')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print(f"Seu nome possui {len(nome.replace(' ', ''))} letras")
lis_nome = nome.split()
print(f'Seu primeiro nome ({lis_nome[0]}) possui {len(lis_nome[0])} letras')
print(f'Seu sobrenome ({lis_nome[-1]}) possui {len(lis_nome[-1])} letras')

nome_low = nome.replace(' ', '').lower()
x_aparece = nome_low.count(nome_low[0])
for letra in nome_low:
    ocorrencia = nome_low[1:].count(letra)
    if ocorrencia > x_aparece:
        mais_aparece = letra
        x_aparece = ocorrencia

if 'mais_aparece' in globals():
    print(f'A letra que mais aparece é a letra "{mais_aparece}", que aparece {x_aparece} vezes')