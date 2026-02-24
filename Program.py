#FIRST PROJECT ON GIT WOOOO(i know its easy dont judge please)

import random

#Sets up the game
def setup():    
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100')
    print('You have 5 chances to guess the correct number\n')

    print('Please select the difficulty level:')
    print('1. Easy (10 chances)\n2. Medium(5 chances)\n3. Hard (3 chances)\n')

    global x
    x = int(input('Enter your choice: '))
    
#Where choice is defined
def decision():
    global x
    if x==1:
        print('You have selected the Easy difficulty! Good luck!\n')
    elif x==2:
        print('You have selected the Medium difficulty! Good luck!\n')
    elif x==3:
        print('You have selected the Hard difficulty! Good luck!\n')
    else:
        print('You have been defaulted to Medium difficulty\n')
        x=2
    


def gamemain():
    global x
    Attempts = 0
    if x==1:
        Attempts = 10
    elif x==2:
        Attempts = 5
    elif x==3:
        Attempts = 3

    ans = random.randint(1,100)
    while Attempts!=0:
        tries = 0
        guess = int(input('Enter your guess: '))
        if ans > guess:
            print(f'Incorrect! The number is more than {guess}.')
            tries+=1
            Attempts -=1
            print(f'Attempts left: {Attempts}\n')
        elif ans < guess:
            print(f'Incorrect! The number is less than {guess}.')
            tries+=1
            Attempts -=1
            print(f'Attempts left: {Attempts}\n')
        elif ans == guess:
            print(f'Congratulations! You guessed the correct number in {tries} attemps!')
            Attempts = 0




setup()
decision()
gamemain()





