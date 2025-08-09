# Day 12

# finding prime number
def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    else:
            num % 1 == 0 and num % num == 0
            return True
            
pri = is_prime(73)
print(pri)

# ================================  DAY 12 PROJECT - GUESS THE NUMBER  ==================================

import random
from art import logo
print(logo)
rand = random.randint(0,100)
EASY = 10
HARD = 5

def easy():
    game = False
    global EASY #declaring EASY as a global variable to access
    print("U have 10 lives to guess the number!")
    while not game:
        if EASY == 0:
            print(f"U have {EASY} lives left, U lose!")
            game = True
        else:
            guess = int(input("Guess a number: "))
            if guess < rand:
                EASY -= 1
                print(f"too low!\nU have {EASY} lives left")
            elif guess > rand:
                EASY -= 1
                print(f"too high\nU have {EASY} lives left")
            elif guess == rand:
                print("Correct! You won!")
                game = True

def hard():
    game = False
    global HARD #declaring HARD as a global variable to access
    print("U have 5 lives to guess the number!")
    while not game:
        if HARD == 0:
            print(f"U have {HARD} lives left, U lose!")
            game = True
        else:
            guess = int(input("Guess a number: "))
            if guess < rand:
                HARD -= 1
                print(f"too low!\nU have {HARD} lives left")
            elif guess > rand:
                HARD -= 1
                print(f"too high\nU have {HARD} lives left")
            elif guess == rand:
                print("Correct! You won!")
                game = True

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm a thinking a number between 1 to 100")
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == 'easy':
        easy()
    elif level =='hard':
        hard()
    else:
        print('Invalid')
game()


    

