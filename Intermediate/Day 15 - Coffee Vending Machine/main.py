
# ================================  DAY 15 PROJECT - COFFEE MACHINE ==================================

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nmoney: ${resources['money']}")

def calculate_coin():
    q = quarters / 4
    d = dimes / 10
    n = nickels / 20
    p = pennies / 100
    a = q+d+n+p
    if a < MENU[chosen]['cost']:
        print("Sorry, that's not enough money. Money refunded")
        return True 
    c = a - MENU[chosen]['cost']
    final_value = "{:.2f}".format(c)
    return final_value

def report_calculation():
    if chosen == 'espresso':
        resources['water'] = resources['water'] - MENU[chosen]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[chosen]['ingredients']['coffee']
        resources['money'] = resources['money'] + MENU[chosen]['cost'] 
    else:
        resources['water'] = resources['water'] - MENU[chosen]['ingredients']['water'] 
        resources['milk'] = resources['milk'] - MENU[chosen]['ingredients']['milk'] 
        resources['coffee'] = resources['coffee'] - MENU[chosen]['ingredients']['coffee']
        resources['money'] = resources['money'] + MENU[chosen]['cost']

def check_requirements():
    if chosen == 'espresso':
        if resources['water'] < MENU[chosen]['ingredients']['water']:
            print("Sorry, there is not enough water")
            return True
    elif resources['coffee'] < MENU[chosen]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee")
            return True
    else:
        if resources['water'] < MENU[chosen]['ingredients']['water']:
            print("Sorry, there is not enough water")
            return True
        elif resources['milk'] < MENU[chosen]['ingredients']['milk']:
            print("Sorry, there is not enough milk")
            return True
        elif resources['coffee'] < MENU[chosen]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee")
            return True

resources['money'] = 0
machine = True 
money = True   
while machine:
    while money:
        coffee = True
        while coffee:  
            chosen = input("What would you like? (espresso/latte/cappuccino): ")
            if chosen == 'off':
                quit()
            if chosen == 'report':
                report()
                chosen = input("What would you like? (espresso/latte/cappuccino): ")
            if check_requirements() == None:
                coffee = False
                
        quarters = int(input("Please insert ur coins\nHow many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        if calculate_coin() == True:
            continue
        else:
            money == False
            break
    
    print(f"Here is ${calculate_coin()} ur change\nHere is ur {chosen} Enjoy! ")
    report_calculation()


 