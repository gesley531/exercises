# Analizador de notas


from time import sleep

fn = float(input('\nplease inform the students first note: '))
sn = float(input('\nNow, inform the second note: '))

calc = (fn + sn) / 2
sleep(2)

if calc >= 7.8:
    print(f'\n\033[0:34mYour average is {calc:.1f}, congratulations YOU were APPROVED!!!\033[m')

elif calc >= 5.5:
    print(f'\n\033[0:33mYour average is {calc:.1f}, welcome to SUMMER SCHOOL my friend!\033[m')

else:
    print(f'\n\033[0:31mYour average is {calc:.1f}, YOU FIRED!!!\033[m')


# END
