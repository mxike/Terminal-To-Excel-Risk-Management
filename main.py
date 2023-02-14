import sys
from rich import print
from os import system
from Tab import Tab

def sheets():
    """
    -Add
    -Remove
    -Change name
    -Give a standard option for each month [{year}month, 2023 januari (as example)] and add all months in 1 go

    Tabs tab = new Tab() 
    tab.add()
    """
    system('cls')
    t1 = Tab().menu()

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

def api():
    """
    -Add API possibility
    -Automatically fill in fields and calculate if its a W/L 
    """
    pass

def settings():
    """
    - Color themes
    - Font
    """
    pass

def exit():
    system('cls')
    print("Goodbye :wave:")
    sys.exit()

def menu_color_title():
    # https://rich.readthedocs.io/en/stable/appendix/colors.html
    colors = []
    pass

def menu_title(name: str, color: str):
    # selected_color = menu_color_title
    # color = selected_color
    print("["+color+"]"+name+"[/"+color+"]")

def display_menu(menu):
    for key, function in menu.items():
        print(key, function.__name__.capitalize())

def create_menu(list):
    menu_items = dict(enumerate(list, start=1))
    display_menu(menu_items)

    select_menu_option = int(input("Select an option: "))
    selected_option = menu_items[select_menu_option]
    selected_option()

def main_menu():
    system('cls')
    main_menu_list = [sheets, titles, api, settings, exit]
    menu_title("Main Menu", "bright_blue")
    create_menu(main_menu_list)

def run():
    while True:
        create_menu(main_menu())

if __name__ == "__main__":
    run()