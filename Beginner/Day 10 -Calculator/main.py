# Day 10

# using return 
def format_name(first_name,last_name):
    if first_name == "":
        return 
    formatted_f_name = (first_name.title())
    formatted_l_name = (last_name.title())
    return f"{formatted_f_name} {formatted_l_name}"
print(format_name(first_name = "jayaseelan",last_name = "b"))

#using title()
def func_1(text):
    return text + text
def func_2(output):
    return output.title()
output = func_2(func_1("hello"))
print(output)

# leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
y1 = is_leap_year(2000)
print(y1)

# ================================  DAY 10 PROJECT - CALCULATOR  ==================================

from art import logo
def add(n1,n2):
    return n1 + n2
    
def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

dict = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide
}

def math():
    print(logo)
    first_num = float(input("what is the first number? : "))
    continue_it = True
    while continue_it:
        for key in dict:
            print(key)
        operation = input("pick an operation : ")
        next_num = float(input("What is the next number? : "))

        answer = dict[operation](first_num,next_num)
        print(f"{first_num} {operation} {next_num} = {answer}")

        continuation = input(f"Type y to continue with {answer} or type n to start a new calculation: ")
        if continuation == 'y':
            first_num = answer
        else:
            print("\n" * 100)
            math()
math()
