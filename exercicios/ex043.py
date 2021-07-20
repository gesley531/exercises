# Indice de massa corporal


print('\n\033[0:33mBody mass index...')


kg = float(input('\n\033[0:33mPlease inform your weight in kg: '))
t = float(input('Now, inform your height (ex: 1.80): '))
imc = kg / (t ** 2)

print(f'\n\033[0:34mYour BMI is {imc:.2f}\033[m')

if imc < 18.5:
    print('-=' * 12)
    print('\033[0:30mYou are \033[0:31mUNDERWEIGHT\033[m')
    print('\033[0:30m-=' * 12)

elif 18.6 <= imc < 25:
    print('-=' * 12)
    print('You are at the \033[0:32mIDEAL WEIGHT\033[m')
    print('-=' * 12)

elif 25 <= imc < 30:
    print('-=' * 12)
    print('Are you \033[0:31mOVERWEIGHT\033[m')
    print('-=' * 12)

elif 30 <= imc < 40:
    print('-=' * 12)
    print('You are \033[0:31mOBESE\033[m')
    print('-=' * 12)

elif imc >= 40:
    print('-=' * 12)
    print('You have \033[0:31mMORBID OBESITY\033[m, please see a doctor... ')
    print('-=' * 12)


# END
