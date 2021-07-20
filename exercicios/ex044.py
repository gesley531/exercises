# Métodos de pagamento

print('\n\033[0:33m===========-\033[0:31mSUPERSTORE\033[0:33m-===========')

for c in range(10):
    value = float(input('\nPlease inform the purchase price: $'))
    print('''\n\033[0:30mPAYMENT METHOD:\033[m
    \033[0:30m[ 1 ]\033[m \033[0:33mPayment in cash
    \033[0:30m[ 2 ]\033[m \033[0:33m1X in credit card
    \033[0:30m[ 3 ]\033[m \033[0:33m2X in credit card
    \033[0:30m[ 4 ]\033[m \033[0:33m3X in credit card\033[m''')

    pm = int(input('\n\033[0:31mInform the payment method: \033[m'))

    if pm == 1:
        calc = (value * 10) / 100
        calc1 = value - calc
        print(f'\n\033[0:33mYou received a 10% discount, the final amount is \033[0:31m${calc1:.2f}\033[m')

    elif pm == 2:
        calc = (value * 5) / 100
        calc1 = value - calc
        print(f'\n\033[0:33mYou received a 5% discont, the final amount is \033[0:31m${calc1:.2f}\033[m')

    elif pm == 3:
        print(f'\n\033[0:33mThis purchase is without discount, the final value is \033[0:31m${value:.2f}\033[m')

    elif pm == 4:
        calc = (value * 20) / 100
        calc1 = value + calc
        print(f'\n\033[0:33mThe final purchase price is \033[0:31m${calc1:.2f}\033[m')

    else:
        print('\n\033[0:31mPlease, select a valid option...\033[m')

# END
