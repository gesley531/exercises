# Gender Analyzer

gender = str(input('\n\033[32mPlease inform your gender [M/W]: ').upper().strip())


while gender != 'M' and gender != 'W' and gender != 'MAN' and gender != 'WOMAN':
    gender = str(input('Please, inform a valid gender: '))


print('\n\033[33mYour gender has been added to the list!')


# END
