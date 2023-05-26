from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_mashine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    
    input_user = input("What would you like: ")
    if input_user == "report":
        coffee_maker.report()
        money_mashine.report()
    elif input_user in ['latte' ,'espresso' ,'cappuccino']:
        drink = menu.find_drink(input_user)
        if coffee_maker.is_resource_sufficient(drink):
           coffee_maker.make_coffee(drink)
        else:
            print("Sorry there is not enough water.")
            is_on = False

