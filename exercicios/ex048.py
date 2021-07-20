# Encontra e soma números impares

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c

print(f'\nO total de numeros encontrados foi {cont} e a soma entre eles é {soma}')
