# Day 11

# ================================  DAY 11 PROJECT - BLACKJACK  ==================================

import random
from art import logo
print(logo)

def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score == 0:
        return "The opponent win with a Blackjack!"
    elif u_score > 21:
        return "Your score is over 21. You lose!"
    elif c_score > 21:
        return "The opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else: 
        return "You lose!"

user_card = []
computer_card = []
is_game = False

for _ in range(2):
    user_card.append(deal_cards())
    computer_card.append(deal_cards())

while not is_game:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"Your cards: {user_card} and current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game = True
    else:
        user_next_move = input("type y to get another card or n to pass: ")
        if user_next_move == 'y':
            user_card.append(deal_cards())
        else:
            is_game = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_cards())
    computer_score = calculate_score(computer_card)

print(f"\nYour final cards are {user_card}, final score: {user_score}")
print(f"The computer's final cards are {computer_card}, final score: {computer_score}")
print(compare(user_score, computer_score))
