# Day 1
#band name generator

city = input("What is the name of the city you grew up in?\n")
pet = input("What is your pet Name?\n")
# print("Your band name is "+city+" "+pet)
print(f"Your Band Name is {city} {pet}")

# \n
print("Hello world\nHello world") # This will print Hello world twice with a newline in between
print(len(input("What is your pet Name?")))  # This will print the length of the input string
username= input("What is your username?\n")
length = len(username)
print(length) # This will print the length of the username input


# Swapping variables
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1)
print(glass2)