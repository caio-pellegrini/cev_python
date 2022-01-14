velo = int(input('Qual a velocidade atual do carro? '))

if velo > 80:
    print('MULTADO! Você está dirigindo acima da velocidade permitida!')
    print(f'Devido a tal ato de irresponsabilidade infringir a Lei, você será multado em R${(velo - 80) * 7 :.2f}')

print('Diriga com segurança e tenha um bom dia!')