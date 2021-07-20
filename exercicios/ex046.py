# Contagem regressiva

from time import sleep
import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print(emoji.emojize('\n:tada:', use_aliases=True))

print('Tada')
