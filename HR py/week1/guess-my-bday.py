from random import randint

name = input("What's your name? ")
guess = 1
month_list = []
year_list = []

while True:
    random_month = randint(1, 12)
    random_year = randint(1989, 2022)
    user_answer = input(
        f'Guess {guess}: {name}, were you born in {random_month}/{random_year}? (yes / no)'
    )
    if user_answer == 'yes':
        break

