# Analizador de triangulos

from time import sleep

print('\n\033[0:32mThis program analyzes triangles, '
      'tells if a triangle is isosceles, scalene or equilateral...')
sleep(2)


l1 = float(input('\n\033[0:35mEnter the first value here: '))
l2 = float(input('Now, the second value: '))
l3 = float(input('To finish, the last value: '))
sleep(2)


if l1 < l2 + l3 and l2 < l1 + l3:
    print('\n\033[0:36mIt is possible to make a triangle\033[m')

    if l1 == l2 == l3:
        print("\033[0:31mThis triangle is EQUILATERAL\033[m")

    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('\033[0:31mThis triangle is SCALENE\033[m')

    else:
        print('\033[0:31mThis triangle is ISOSCELES\033[m')


else:
    print('\n\033[0:33mCannot form a triangle\033[m')


# END
