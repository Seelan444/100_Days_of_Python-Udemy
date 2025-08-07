# Day 2

print(len("st"))
print("The numbers of letter in your name:", len(input("What is your name? ")))

#mathematical operations
print(3 + 5)  # Addition
print(7 - 4)  # Subtraction 
print(3 * 2)  # Multiplication
print(6 / 3)  # Division
print(6//3)  # Floor Division
print(2 ** 3)  # Exponentiation

#pemdas
print(3 * (3 + 3) / 3 - 3)  # Parentheses first, then Multiplication, Division, Addition, Subtraction
print(3 * 3 + 3 / 3 - 3)  # Order of operations: Multiplication, Division, Addition, Subtraction


# BMI Calculator
# Create a variable called height in meters and weight in kilograms.
height = 1.65 
weight = 84
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
print(bmi)
print(round(bmi))  # Round the result to 2 decimal places

age = 10
print(f"Your age is  {age}")#formatted strings

# =======================  DAY 9 PROJECT - TIP CALCULATOR   ======================================

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the total bill with tip
bill_with_tip = tip_percentage / 100 * bill + bill

# Calculate the amount per person  
amount_per_person = bill_with_tip / people
total_amount = round(amount_per_person, 2)  # Round to 2 decimal places
print(f"Each person should pay: ${total_amount}")  # Format to 2 decimal


