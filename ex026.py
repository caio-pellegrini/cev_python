frase = input('Digite uma frase: ').strip().lower()
print(f'A frase possui {len(frase) - frase.count(" ")} letras')
print(f'A letra A aparece {frase.count("a")} vez(es)')
if frase.count("a") > 0:
    print(f'A primeira letra A aparece na posição {frase.find("a") + 1}')
    print(f'A última letra A aparece na posição {frase.rfind("a") + 1}')
