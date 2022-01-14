frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
frase_invertida = frase[::-1]
print(f'A frase {frase} invertida é {frase_invertida}')
if frase == frase_invertida:
    print('É um palíndromo!!')
else:
    print('Não é um palíndromo :(')
