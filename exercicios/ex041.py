# Categoria de competição

from datetime import date
from time import sleep


print('\n\033[0:31mWelcome to olympic games, find you category to compete...\033[m')
year = date.today().year
sleep(1)

yo = int(input('\n\033[0:33mInform your year of birth: \033[m'))
sleep(1)

calc = year - yo

if calc <= 9:
    print(f'\n\033[0:34mYou have {calc} years, you compete in the CHILDRENS category')

elif calc <= 14:
    print(f'\n\033[0:34mYou have {calc} years, you compete in the JUNIOR category')

elif calc <= 19:
    print(f'\n\033[0:34mYou have {calc} years, you compete in the GYM CLASS category')

elif calc <= 25:
    print(f'\n\033[0:34mYou have {calc} years, you compete in the PROFESSIONAL category')

elif calc >= 26:
    print(f'\n\033[0:34mYou have {calc} years, you compete in the MASTERS category\033[m')


# END
