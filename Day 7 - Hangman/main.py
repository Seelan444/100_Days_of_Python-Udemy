#Day 7
#hangman

import random
from hangman_words import word_list
from hangman_art import stages, logo
                                    

print(logo)
fruit = ['apple', 'banana', 'watermelon','mango']

selected_fruit = random.choice(fruit)
# print(selected_fruit)

place_holder = ""
length = len(selected_fruit)

for postion in range(length):
    place_holder += "_"
print(place_holder)

game_over = False
corrected_letter = []
lives = 6

while not game_over:
    guess = input("Make a guess: ").lower()

    if guess in corrected_letter:
        print(f"you already guessed {guess}")

    display = ""
    for letter in selected_fruit:
        if letter == guess:
            display += letter
            corrected_letter.append(guess)
        elif letter in corrected_letter:
            display += letter
        else:
            display += "_"
            
        
    print(display)
    if "_" not in display:
        game_over = True
        print('You win')

    if guess not in corrected_letter:
       lives -= 1
       print(f"You guessed the {guess}, it's not in the word, you lose a life")
       if lives == 0:
           game_over
           print('You lose') 

    print(stages[lives])