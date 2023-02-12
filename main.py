import sys
from rich import print
from os import system

def tabs():
    """
    -Add
    -Remove
    -Change name
    -Menu func

    Tabs tab = new Tab() 
    tab.add()
    """
    pass

def titles():
    """
    -Add single title
    -Add multiple titles
    -Insert standard title set
    -Change title
    -Delete title
    -Clear all titles
    """
    pass

def exit():
    system('cls')
    print("Goodbye :wave:")
    sys.exit()

def display_menu(menu):
    for key, function in menu.items():
        print(key, function.__name__.capitalize())

def run():
    function_names = [tabs, titles, exit]
    menu_items = dict(enumerate(function_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(input("Where to go, select an option: "))
        selected_value = menu_items[selection]
        selected_value()

if __name__ == "__main__":
    run()
    