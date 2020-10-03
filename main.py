import random
from playsound import playsound
Player1 = input("Enter your name Player1: ")
Player2 = input("Enter your name Player2: ")


def role():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 < dice2:
        return dice2
    elif dice1 > dice2:
        return dice1
    elif dice1 == dice2:
        return dice1


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return Player1
    else:
        return Player2


def replay():
    choice = input('Do you want to repplay? Type yes or no: ').lower()
    return choice == 'yes' or choice == 'y'


print('Welcome to Roll The Dice')
while True:
    Player1Dice = role()
    Player2Dice = role()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input("Are you ready to play? Type Yes or No: ").lower()
    if play_game == 'yes' or play_game == 'y':
        game_mod = True
    else:
        game_mod = False
        
    while game_mod:
        playsound('Shake And Roll Dice.wav')
        if Player1Dice > Player2Dice:
            print(f'{Player1} has scored {Player1Dice} and win \U0001F3C6	- {Player2} scored {Player2Dice} and loss ')
            game_mod = False
        elif Player1Dice < Player2Dice:
            print(f'{Player2} has scored {Player2Dice} and win \U0001F3C6 - {Player1} scored {Player1Dice} and loss ')
            game_mod = False
        else:
            print(f'{Player1} has scored {Player1Dice} and is equal with {Player2} scored {Player1Dice} and It''s a draw! ')
            game_mod = False
    if not replay():
        break
