frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
frase_invertida = []
for letra in range(len(frase), 0, -1):
    frase_invertida.append(frase[letra - 1])
frase_invertida = ''.join(frase_invertida)
print(f"A frase {frase} invertida é {frase_invertida}")
if frase == frase_invertida:
    print('É UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO')
