print('----- CALCULADORA IMC -----')
peso = float(input("Qual é o seu peso? (em Kg) "))
altura = float(input('Qual é a sua altura? (em m) ').replace(',', '.'))
imc = peso / altura**2
print(f'O IMC é {imc :.1f}')
if imc < 18.5:
    status = {'status': '\033[34mABAIXO DO PESO\033[m',
              'frase': 'Consulte um médico ou nutricionista.'}
elif imc <= 25:
    status = {'status': '\033[32mPESO IDEAL\033[m',
              'frase': 'Parabéns!'}
elif imc <= 30:
    status = {'status': '\033[33mSOBREPESO\033[m',
              'frase': 'Melhore sua alimentação e faça mais exercícios!'}
elif imc <= 40:
    status = {'status': '\033[36mOBESIDADE\033[m',
              'frase': 'Cuidado, é melhor você procurar um médico.'}
else:
    status = {'status': '\033[31mOBESIDADE MÓRBIDA\033[m',
              'frase': 'Você deve procurar ajuda urgente!'}
print(f'Seu status é: {status["status"]}. {status["frase"]}')