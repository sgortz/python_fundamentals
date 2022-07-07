# REQUIREMENTS:
# Asks your name with the prompt "Hi! What is your name?"
# f the computer guesses it correctly because you respond yes, it prints the message I knew it! and stops guessing

from random import randint

name = input("What's your name? ")
guess = 1

while True:
    random_month = randint(1, 12)
    random_year = randint(1924, 2004)
    user_answer = input(
        f'Guess {guess}: {name}, were you born in {random_month}/{random_year}? \n (yes / no) '
    )
    if user_answer == 'yes':
        print('I knew it')
        break
    elif user_answer == 'no' and guess < 4:
        guess += 1
        print('Drat! Lemme try again!')
    else:
        print('I have other things to do. Good bye.')
        break