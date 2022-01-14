"""import math

an = float(input('Digite o ângulo que você deseja: '))
ra = math.radians(an)
print(f'O ângulo de {an}° tem o SENO de {math.sin(ra) :.2f}')
print(f'O ângulo de {an}° tem o COSSENO de {math.cos(ra) :.2f}')
print(f'O ângulo de {an}° tem a TANGENTE de {math.tan(ra) :.2f}')"""

import math

an = math.radians(float(input('Digite o ângulo que você deseja: ')))
print(f'SENO = {math.sin(an) :.2f}')
print(f'COSSENO = {math.cos(an) :.2f}')
print(f'ANGENTE = {math.tan(an) :.2f}')
