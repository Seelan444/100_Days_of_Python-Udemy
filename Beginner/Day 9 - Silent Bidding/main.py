# Day 9
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_scores['Draco'] = "oo"  #to change the value of the key
print(student_scores['Draco'])

#grading students based on their marks
student_grade = {}
for key in student_scores:
    value = student_scores[key]
    if value >= 91:
        student_grade[key] = "Excellent"
    elif value >= 81 and value < 91:
        student_grade[key] = "super"
    elif value >= 71 and value < 81:
        student_grade[key] = "Okay"
    elif value < 71:
        student_grade[key] = "Fail"
print(student_grade)

#nested list
nest_list = ['1','2',['3','4']]
print(nest_list[-1][1])

#accessing key and values in a dictionary
country = {
    "india":{
        "city":["chennai","covai"],
        "no_of_time_visited":4
    }
}
print(country["india"]["city"][1])
print(country["india"]["no_of_time_visited"])


# ======================   DAY 9 PROJECT - BIDDING [TRIED VERSION] =======================================

from art import logo
print('Welcome to the secret auction program ')
print(logo)

bidders = {}
values_list = []

def bid_calc(key,bid):
    bidders.setdefault(key, bid)
    print(bidders)
    
it = True
while it:
    name = input("What is ur name?\n")
    bidding_amount = int(input("What is ur bid? : $\n"))
    bid_calc(name,bidding_amount)

    for key in bidders:
        value = bidders[key]
        values_list.append(value)
    print(values_list)

    fellows = input("Are there any other bidders? Type 'yes' or 'no\n")
    print("\n" * 100)
    if fellows == 'no':
        greatest_number = values_list[0]
        for i in (values_list):
            if i > greatest_number:
                greatest_number = i
        for key in bidders:
            value = bidders[key] 
            if greatest_number == value:
                print(f"The winner is {key} and bid is ${greatest_number}")
        it = False


# ================================  CORRECT VERSION OR EASIER VERSION  ==================================

from art import logo
print('Welcome to the secret auction program ')
print(logo)

bidders = {}
highest_bid = 0

it = True
while it:
    name = input("What is ur name?\n")
    bidding_amount = int(input("What is ur bid? : $\n"))
    bidders[name] = bidding_amount

    fellows = input("Are there any other bidders? Type 'yes' or 'no\n")
    print("\n" * 100)
    if fellows == 'no':
        for key in bidders:
            value = bidders[key]
            if value > highest_bid:
                highest_bid = value 
                winner = key
        print(f"The winner is {winner} and the bid is ${highest_bid}")
        it = False



    




