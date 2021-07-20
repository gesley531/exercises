# Complete analyzer
from typing import Any

contid = 0
maioridade = 0
nomevelho = ''
menoridade = 0

p: int
for p in range(1, 5):
    print(f'\n\033[36m======-{p}ªPeople-=======\033[m')
    nome = str(input('\n\033[33mEnter your name: ').title().strip())
    idade = int(input('Enter your age: '))
    sexo = str(input('Inform your gender (M/F): ').upper())
    contid += idade
    if p == 1:
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        menoridade += 1
    r = str(input('Do you want to continue?? [S/N]: '.upper()))

midade = contid / p


print(f'\n\033[31mThe average age is {midade} years!')
print(f'The oldest MAN is {nomevelho} and he is {maioridade}')
print(f'Altogether we have {menoridade} women under 20!')


# END
