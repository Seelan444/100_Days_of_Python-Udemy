import random

# random_number = random.randint(0, 1)
# if random_number == 0:
#     print("Heads")
# else:       
#     print("Tails")

# #one way
# people = ['seelan', 'sam','reegs','jey'] 
# random_people = random.randint(0, 3)
# print(people[random_people])

# #other way
# print(random.choice(people))  # This will randomly select one person from the list


# #practice
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1])#this will print the vegetables list
# print(dirty_dozen[0])#this will print the fruits list

# print(dirty_dozen[1][1]) # This will print "kale"


#rock paper scissors #this is full of my own way
hand_gestures = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']


print("Welcome to Rock, Paper, Scissors!")
game_signs = ['rock','paper','sciccors']

computer = (random.choice(game_signs))

#user's choice
user_choice = (input("what do u choose? Type rock, paper, scissors\n\nUr choice: "))
print(hand_gestures[game_signs.index(user_choice)])

#computer's choice
print(f"Computer choice: {computer} ")
print(hand_gestures[game_signs.index(computer)])

if user_choice not in game_signs:
       print('Invalid')
if computer == 'rock' and user_choice == 'rock':
    print("It's a draw")
elif computer == 'rock' and user_choice == 'paper':
    print('U Win')
elif computer == 'rock' and user_choice == 'sciccors':
        print('U Lose')
elif computer == 'paper' and user_choice == 'rock':
        print('U Lose')
elif computer == 'paper' and user_choice == 'paper':
        print("It's a draw")
elif computer == 'paper' and user_choice == 'sciccors':
        print('U Win')
elif computer == 'sciccors' and user_choice == 'rock':
        print('U Win')
elif computer == 'sciccors' and user_choice == 'paper':
        print('U Lose')
elif computer == 'sciccors' and user_choice == 'sciccors':
        print("It's a draw")
print()
