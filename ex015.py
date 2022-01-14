kms = float(input('Quantos km o carro andou? '))
dias = int(input('Quantos dias o carro foi alugado? '))
valor = (60 * dias) + (0.15 * kms)
print(f'O valor que esse carro terá de pagar é R${valor :.2f}')