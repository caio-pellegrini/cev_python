lar = float(input('Qual a largura da parede? '))
alt = int(input('Qual a altura da parece? '))

print(f'\nSua parede tem a dimensão de {lar :0.2f}m x {alt :0.2f}m.')
area = lar*alt
print(f'Isso significa que sua área é de {area :0.2f}m².')

print(f'\nPara pintar essa parede, você precisará de {area/2 :0.2f}l de tinta')
