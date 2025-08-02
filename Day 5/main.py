#for loop

students_score = [55, 66, 77, 88, 99, 100, 67, 85,34,]
max_score = 0
for score in students_score:
    if score > max_score:
     max_score = score
print(max_score)


total = 0
for i in range(1, 101):
    total += i
print(total)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

user_letters = int(input("how many letters do u want? "))
user_number = int(input("how many numbers do u want? "))
user_symbol = int(input("how many symbols do u want? "))

#easy level
passw = ''

for char in range(0, user_letters):
    passw += random.choice(letters)
for char in range(0, user_number):
    passw += random.choice(numbers)
for char in range(0, user_symbol):
    passw += random.choice(symbols)
print(passw)


#hard level
pass_list = []
for char in range(0, user_letters):
    pass_list.append(random.choice(letters))
for char in range(0, user_number):
    pass_list.append(random.choice(numbers))
for char in range(0, user_symbol):
    pass_list.append(random.choice(symbols))

#to shuflle list
random.shuffle(pass_list)

# to list into str
password = ''
for char in pass_list:
    password += char
print(password)