weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
print(bmi)
if bmi < 18.5:
   print("underweight")
elif bmi >= 18.5 and bmi < 25:
         print("normal weight")
else:
     bmi >= 25
     print("overweight")


#pizza order
print("Welcome to Python Pizza Deliveries!") 
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# Calculate the bill based on the size and toppings
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
        bill += 20
elif size == 'L':
        bill += 25
if add_pepperoni == 'Y':
    if size == 'S':
          bill += 2
    else:
          bill += 3
if extra_cheese == 'Y':
         bill += 1
else:
      print("Invalid size selected.")
print(f"Your final bill is: ${bill}.")


#treasure island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go left or right? (left/right)\n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim across or wait for a boat? (swim/wait)\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose? (red/yellow/blue)\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")
# This is a simple text-based adventure game where the player makes choices to find a treasure.