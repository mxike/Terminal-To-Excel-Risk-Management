from os import system
import openpyxl

class Tab:
  def showTabs(self):
    pass

  def addTab(self):
    system('cls')
    print("add Tab")
    self.menu()

  def changeTab(self):
    pass

  def removeTab(self):
    pass

  def back(self):
    from main import main_menu
    main_menu()

  def menu(self):
    from main import create_menu, menu_title
    menu_title("Tab Menu", "bright_blue")
    tab_menu = [self.showTabs, self.addTab, self.changeTab, self.removeTab, self.back]

    create_menu(tab_menu)
    