from datetime import datetime
print('\033[1;31m---- TESTE DE ALISTAMENTO MILITAR ----\033[m')
atual = datetime.today().year
sexo = input('Você é homem ou mulher? (h / m) ').strip().lower()
if sexo == 'h' or sexo == 'homem':
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    alist = 18
    print(f'Quem nasceu em {nascimento} tem (ou vai completar) {idade} anos em {atual}')
    if idade < alist:
        falta = alist - idade
        print(f'Ainda faltam {falta} {"ano" if falta == 1 else "anos"} para o alistamento')
        print(f'Seu alistamento será em {atual + falta}')
    elif idade == alist:
        print('Você precisa se alistar nesse ano! (Caso não seja Testemunha de Jeová)')
    elif idade > alist:
        passou = idade - alist
        print(f'Você já deveria ter se alistado há {passou} {"ano" if passou == 1 else "anos"}')
        print(f'Seu alistamento foi em {atual - passou}')
elif sexo == 'm' or sexo == 'mulher':
    print('Você não precisa se alistar')
else:
    print('Foi mal, não entendi.')
