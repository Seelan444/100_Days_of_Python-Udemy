# Day 16

# Object Oriented Programming - OOP
# from turtle import Turtle, Screen
# from prettytable import PrettyTable
# table = PrettyTable()

# table.field_names = ["S.No", "Data"]
# table.add_rows(
#     [
#         [1,"Data"],
#         [2,"Data"],
#     ]
# )
# table.align = "l"
# print(table)

# tur = Turtle()
# print(tur)
# tur.shape("turtle")
# tur.color("green")
# tur.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# ================================  DAY 16 PROJECT - COFFE VENDING MACHINE - OOP ==================================

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine = True
while machine:
    chosen = input(f"What would you like? {menu.get_items()}: ")
    if chosen == 'off':
        machine = False
    elif chosen == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(chosen)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
