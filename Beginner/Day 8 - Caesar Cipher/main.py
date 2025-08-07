#Day 8
def greet():
    print('a')
    print('b')
    print('C')
greet()

# Life in weeks
def life_in_weeks(age):
    years = 90 - age #remaining years
    weeks = years * 52 #remaining weeks
    print(f"You have {weeks} weeks left.")
life_in_weeks(22)


# Love calculator (My version - doesn't print the repeated letters count)
def calculate_love_score(boy_name,girl_name):
    word1 = "true"
    word2 = "love"
    score1 = 0
    score2 = 0

    for i in word1:
        if i in boy_name:
            score1  += 1
        elif i in girl_name:
            score1  += 1

    for i in word2:
        if i in boy_name:
            score2  += 1
        elif i in girl_name:
            score2  += 1 

    score1 = str(score1)
    score2 = str(score2)
    score = score1 + score2
    print(score)
calculate_love_score("seelan","unknown")


# correct version
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    score = int(str(first_digit) + str(second_digit))
    print(score)  
calculate_love_score("seelan","unknown")

# ================================  DAY 8 PROJECT - CAESER [TRIED VERSION]  =======================================

option = input("Type encrypt to encrypt or decrypt to decrypt\n").lower()
text = input("Type your message:\n").lower()
shift_num = int(input('Type your shift number:\n'))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word,shift):
    encryption = ""
    for i in word:
        shifted_position = alphabet.index(i) + shift
        shifted_position %= len(alphabet)
        encryption += alphabet[shifted_position]
    print(f"Your encnrypted word is {encryption}")

def decrypt(word,shift):
    decryption = ""
    for i in word:
        shifted_position = alphabet.index(i) - shift
        decryption += alphabet[shifted_position]
    print(f"Your decrypted word is {decryption}")

def ceaser(encrypt,decrypt):
    if option == 'encrypt':
        encrypt(word = text,shift = shift_num)
    else:
        decrypt(word = text,shift = shift_num) 
ceaser(encrypt,decrypt)


# ================================  CORRECT VERSION OR EASIER VERSION  ==================================

from art import logo
def ceaser(word,shift,encrypt_or_decrypt):
    output = ""
    if encrypt_or_decrypt == 'decrypt':
              shift *= -1
    for i in word:
        if i not in alphabet:
            output += i
        else:
            shifted_position = alphabet.index(i) + shift
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
    print(f"Your {option}ed word is {output}")
    
should_continue = True

while should_continue:
    print(logo)
    option = input("Type encrypt to encrypt or decrypt to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift_num = int(input('Type your shift number:\n'))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ceaser(text,shift_num,option)
            
    again = input("If u want go again type 'yes' otherwise type 'no'\n").lower()
    if again == 'no':
        should_continue = False
        print("Goodbye")
