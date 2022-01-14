from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto. Digite 0 para ver o ano atual '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[32m{ano}\033[m é \033[36mbissexto')
else:
    print(f'O ano \033[31m{ano}\033[m não é \033[36mbissexto')