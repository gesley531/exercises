# Guess the number

from random import randint


computer = randint(1, 10)
t = int(input('\n\033[33mGuess the number i am thinking between 1 and 10: '))
c = 1

if t > 10:
    t = int(input('\033[31mInform a number between 1 and 10: '))
    c += 1

while computer != t:
    if t > computer:
        t = int(input('\033[33mIs a lower value, try again: '))
        c += 1
    if t < computer:
        t = int(input('\033[33mIs a higher value, try again: '))
        c += 1
    if t > 10:
        t = int(input('\033[31mInform a number between 1 and 10: '))
        c += 1
print(f'\n\033[36mCongratulations, i am thinking in {computer}, you got it right in {c} tries')

# END
