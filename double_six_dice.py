import random

print('___________________________')
print('|                          |')
print('|   Double Six Dice Game   |')
print('|__________________________|')
print()

player1 = input('What is your name: ')


dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


P1counter = 0

while (dice1 + dice2 != 12):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    P1counter += 1

print(f'number of tries {P1counter}')

print()

player2 = input('What is your name: ')


dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


P2counter = 0

while (dice1 + dice2 != 12):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    P2counter += 1

print(f'number of tries {P2counter}')

if P1counter < P2counter:
    print(f'{player1} is the winner with: {P1counter} tries')
else:
    print(f'{player2} is the winner with: {P2counter} tries')
