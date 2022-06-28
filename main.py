from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:


coffee_maker.is_resource_sufficient()
money_machine.process_coins()

