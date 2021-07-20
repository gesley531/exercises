# Jokenpô

from random import randint
from time import sleep


print('\n\033[0:33mEae, vamos jogar jokenpô? ')

# FUNCIONAMENTO
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
sleep(1)


# OPÇÕES
print('''\n\033[0:33mOpções:\033[m
\033[0:31m[0] Pedra
[1] Papel
[2] Tesoura\033[m''')
sleep(1)

jog = int(input('\n\033[0:33mSelecione uma opção: '))
sleep(1)


# IF, ELSE E ELIFS
if jog > 2:
    print('\n\033[0:31mOPÇÃO INVALIDA...')

else:
    print('JO')
    sleep(1)
    print("KEN")
    sleep(1)
    print('PÔ!!!')

    print('\033[0:31m-=' * 15)
    print(f'\033[0:33mcomputador jogou {itens[computador]}')
    print(f'\033[0:33mVocê jogou {itens[jog]}')
    print('\033[0:31m-=' * 15)

    if computador == 0:  # pedra
        if jog == 0:
            print('\033[0:33mO JOGO EMPATOU...')
        elif jog == 1:
            print('\033[0:32mO JOGADOR VENCEU!!!')
        elif jog == 2:
            print('\033[0:33mO COMPUTADOR VENCEU!!!')

    if computador == 1:  # papel
        if jog == 0:
            print('\033[0:32mO computador VENCEU!!!')
        elif jog == 1:
            print('\033[0:33mO JOGO EMPATOU...')
        elif jog == 2:
            print('\033[0:32mO JOGADOR VENCEU!!!')

    if computador == 2:
        if jog == 0:
            print('\033[0:32mO JOGADOR VENCEU!!!')
        elif jog == 1:
            print('\033[0:32mO COMPUTADOR VENCEU!!!')
        elif jog == 2:
            print('\033[0:33mO JOGO EMPATOU...')


# END
