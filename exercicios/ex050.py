# Encontra e soma números pares

soma = 0
cont = 0

c: int
for c in range(1, 7):
    numero = int(input(f'\nDigite o {c}° número: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1


print(f'\n\033[0:33mForam encontrados {cont} números pares e a soma deles é {soma}')

# END
