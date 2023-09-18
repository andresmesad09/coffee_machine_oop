from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
must_continue = True
while must_continue:
    order_name = input(f"What would you like? ({menu.get_items()}): ")
    if order_name == "off":
        print("bye")
        break
    elif order_name == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        # check resources
        if coffee_machine.is_resource_sufficient(drink):
            # payment
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_machine.make_coffee(drink)




