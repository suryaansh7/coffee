from menu import Menu

from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

s=input("enter coffee of ur choice")
if(s=="report"):
    print(coffee.report())

