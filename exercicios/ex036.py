# Analyzer empresses

from time import sleep


print('\n\033[0:31mhello user, if you need a loan, please inform your data below...\033[m')
sleep(2)

print('Remember that the installment amount cannot exceed 30% of your salary.')
sleep(2)


# User Data
name = str((input('\n\033[0:33mPlease inform your full name: ').strip()).title())
sn = (name.split())  # simple name

value = float(input('\nPlease inform the requested amount: $'))
sleep(1)

cash = float(input('\nPlease inform your current salary: $'))
sleep(1)

year = int(input('\nIn how many years do you want to pay?: '))
sleep(1)

# Calculator

c1 = year * 12

c2 = value / c1

c3 = (cash * 30) / 100

print(f'\n\033[0:36mIn this simulation, the monthly installment amount would be ${c2:.2f}\033[m')
sleep(2)

if c3 <= c2:
    print(f'\n\033[0:31mSorry, mr.{sn[0]} the payment was not approved...\033[m')

else:
    print(f'\n\033[0:32mCongratulations mr.{sn[0]} '
          f'the payment was approved, '
          f'please contact the institution manager and confirm the loan.\033[m')

# END.
