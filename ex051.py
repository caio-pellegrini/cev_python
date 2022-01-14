# igual mostrado na aula
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
    print(c, end=' → ')
print('ACABOU')