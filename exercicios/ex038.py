# Analizador de números


n1 = int(input('Please insert a number: '))
n2 = int(input('Now, insert another number: '))

if n1 > n2:
    print('\nThe first number is greater than the second')

elif n1 == n2:
    print('\nThere is no greater value, the two values are equal')

else:
    print('\nThe second number is greater than the first')
