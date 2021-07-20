# AP generator

print('\n\033[31mArithmetic Progression')
print('-=' * 10)

ft = int(input('\033[33mFirst Term: '))
r = int(input('Reason: '))
term = ft
cont = 1

while cont <= 10:
    print(f'{term} => ', end='')
    term += r
    cont += 1

print('\033[31mEND')


# END
