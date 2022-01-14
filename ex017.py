from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenusa vai medir {h :.2f}')
# print(f'A hipotenusa vai medir {(co**2 + ca**2) ** (1/2)}')
print(f'Podemos ter certeza disso, pois {co}² + {ca}² = raiz de {(co**2 + ca**2)} = {h}')
