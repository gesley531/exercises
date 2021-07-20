# Analizador de maioridade


from datetime import date


cont = 0
cont1 = 0
today = date.today().year


for c in range(1, 8):
    idade = int(input(f'\n\033[33mDigite o ano de nascimento da {c}ª pessoa: '))
    calc = today - idade
    if calc >= 18:
        cont1 += 1

    elif calc < 18:
        cont += 1


print(f'\n\033[31mTemos {cont1} pessoas maiores de idade')
print(f'Temos {cont} pessoas menores de idade')


# END
