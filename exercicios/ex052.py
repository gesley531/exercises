# Detector de números primos

num = int(input('\nDigite um número: '))
print('\n')


tot = 0


for c in range(1, num + 1):
    if num % c == 0:
        print('\033[0:33m', end=' ')
        tot += 1

    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')


if tot >= 3:
    print(f'\n\nO número {num} foi dividido {tot} vezes!!!')
    print(f'ESTE NÚMERO NÃO É PRIMO ')

else:
    print(f'\n\nO número {num} foi dividido {tot} vezes!!!')
    print(f'ESTE NÚMERO É PRIMO ')


# END
