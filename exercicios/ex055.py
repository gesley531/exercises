# Rastreador de pesos

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'\n\033[36mDigite o {p}ª peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f"\n\033[33mO maior peso encontrado foi {maior:.2f}kg,"
      f" e o menor peso encontrado foi {menor:.2f}kg")

# END
