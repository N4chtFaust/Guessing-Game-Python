import random

# START

random = random.randint(1, 100)  # PREPARATION

com = '''
Welcome to Guessing Game!
You have 10 attempts to play the game.
Try to guess number between 1-100 good luck!
'''
print(com)

x = False
attempt = 1
while attempt <= 10:
    gues = input(f'Attempt #{attempt}: Try to guess a number between 1-100: ')
    print(random)
    if gues.isdigit():
        attempt += 1
        gues = int(gues)
        if gues == random:
            x = True
            break
        elif gues > random:
            print('Higher!')
        else:
            print('Lower')
    else:
        print('Please enter a number.')

if x:
    print(f'\nCongrats you guess the number {random} in Attempt {attempt -1}.')
else:
    print(f'\nGame over!! The random number is {random}.')


