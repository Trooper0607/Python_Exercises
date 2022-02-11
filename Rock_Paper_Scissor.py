#Rock Paper Sciccors

import random

answer = random.choice(['Rock', 'Paper', 'Scissor']).lower()
print(answer)

guess = input("Rock, Paper or Scissors? ")

if guess == 'rock':
    if answer == 'paper':
        print(f"{answer} covers {guess} you lose")
    elif answer == 'scissor':
        print(f"{guess} smashes {answer}! YOU WIN!!!")
    elif answer == 'rock':
        print(f"{guess} and {answer} cancels out! its a draw!")
    else:
        print(f"You entered: {guess}, enter a valid input")

if guess == 'paper':
    if answer == 'paper':
        print(f"{guess} and {answer} cancels out! its a draw!")
    elif answer == 'scissor':
        print(f"{answer} cuts {guess}! You Lose")
    elif answer == 'rock':
        print(f"{guess} covers {answer}, YOU WIN!!!")
    else:
        print(f"You entered: {guess}, enter a valid input")

if guess == 'scissor':
    if answer == 'paper':
        print(f"{guess} cuts {answer}, YOU WIN!!!")
    elif answer == 'scissor':
        print(f"{guess} and {answer} cancels out! its a draw!")
    elif answer == 'rock':
        print(f"{answer} smashes {guess}, You Lose")
    else:
        print(f"You entered: {guess}, enter a valid input")
