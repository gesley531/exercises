# First Menu


from time import sleep


n1 = int(input('\n\033[36mEnter a number: '))
n2 = int(input('Now enter a number again: '))

choice = 0

while choice != 5:
    sleep(1)
    print('\n\033[31mWhat are you doing with these numbers?'
          '\033[33m\n[1]-Want to add?'
          '\n[2]-Do you want to multiply?'
          '\n[3]-The biggest number'
          '\n[4]-New numbers'
          '\n[5]-Finish the program')
    sleep(1)
    choice = int(input('\nEnter your choice: '))

    if choice == 1:
        sleep(1)
        print(f'{n1} + {n2} = {n1 + n2}')
        print('-' * 20)
        sleep(1)

    if choice == 2:
        sleep(1)
        print(f'{n1} X {n2} = {n1*n2}')
        print('-' * 20)
        sleep(1)

    if choice == 3:
        if n1 > n2:
            sleep(1)
            print(f'\033[31m{n1} Is bigger than {n2}')
            print('-' * 20)
            sleep(1)
        elif n1 == n2:
            sleep(1)
            print('\033[31mThe values are the same')
            print('-' * 20)
            sleep(1)
        else:
            sleep(1)
            print(f'\033[31m{n2} Is bigger than {n1}')
            print('-' * 20)
            sleep(1)

    if choice == 4:
        sleep(1)
        n1 = int(input('\n\033[33mEnter a number: '))
        n2 = int(input('Now enter a number again: '))
        sleep(1)

    if choice == 5:
        print('\n\033[33mFinishing...')
        sleep(3)
        print('Thanks for using the program, come back often')
        sleep(1)

    else:
        sleep(1)
        print('\033[31mInvalid option, try again...')
        print('-' * 20)
        sleep(1)


# END
