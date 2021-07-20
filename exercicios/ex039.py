# Alistamento Militar

from datetime import date

yo = int(input('Inform your year of birth: '))

today = date.today().year

c = today - yo

if c < 17:
    print('\033[0:31mNo need to enlist yet.\033[m')

elif c == 17:
    print('\033[0:33mYou are not required to enlist yet, but if you wish, you can do so now.\033[m')

elif 18 <= c < 63:
    print('\033[0:32mYou must apply as soon as possible or ask to be dismissed as soon as possible.'
          ' \nYou can do this at any military base in your city.\033[m')

elif c >= 63:
    print('\033[0:36mTime has passed, it is no longer possible to subscribe...\033[m')

# END
