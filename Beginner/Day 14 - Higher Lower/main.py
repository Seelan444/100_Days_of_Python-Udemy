
# ================================  DAY 14 PROJECT - HIGHER LOWER ==================================

import random
from game_data import data 
from art import logo
from art import vs

def get_random_acc():
    """ gets a random account from the data list """
    return random.choice(data)

def option_sentence(option):
    """ to return the account deatils without follower's count"""
    return f"{option['name']}, {option['description']}, {option['country']}"

def game ():
    game_over = False
    score = 0
    print("welcome to Higher Lower Game")
    print(logo)
    while not game_over:
        option_a = get_random_acc()
        print(f"Compare A : {option_sentence(option_a)}")
        print(vs)
        option_b = get_random_acc()
        while option_a == option_b:
            option_b == get_random_acc()
        print(f"Compare B : {option_sentence(option_b)}")
        print()
        guess = input("Who has more followers? Type A or B: ").lower()
        print()
        a = option_a['follower_count']
        b = option_b['follower_count']
        if guess == 'a' and a > b:
            score += 1
            print(f"U r right! current score {score} ")
            print()
        elif guess == 'a' and b > a: 
            print(f"U r wrong! {option_a['name']}'s follower count: {option_a['follower_count']}, {option_b['name']}'s follower count: {option_b['follower_count']}\nUr final score {score} ")
            return True
        elif guess == 'b' and b > a:
            score += 1
            print(f"U r right! current score {score} ") 
            print()
        elif guess == 'b' and a > b: 
            print(f"U r wrong! {option_a['name']}'s follower count: {option_a['follower_count']}, {option_b['name']}'s follower count: {option_b['follower_count']}\nUr final score {score} ")
            return True    
        else:
            print("Invalid")
            return True
game()