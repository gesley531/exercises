# Detector de palíndromo


frase = str(input('\n\033[33mDigite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]


print(junto, inverso)


if inverso == junto:
    print('\033[31mEstá frase é um PALÍNDROMO!!!')
else:
    print('\033[31mEstá frase NÃO É UM PALINDROMO!!!')


# END
