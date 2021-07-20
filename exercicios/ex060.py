n = int(input('\n\033[36mEnter a number and I show the factorial value: '))
c = n
f = 1

print(f'\033[31mCalculating {n}! = ', end='')
while c > 0:
    print(f'\033[33m{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')

    f = f * c
    c -= 1

print(f'{f}')

# END
