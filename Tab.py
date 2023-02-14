import os, time
from os import system
from dotenv import load_dotenv
from openpyxl import Workbook, load_workbook

load_dotenv()
wb = load_workbook(os.getenv('FILE_PATH'))

class Tab:
  def showSheets(self):
    system('cls')
    print("Active worksheet: ", wb.active)
    print("All worksheets: ", wb.sheetnames)
    print()
    self.menu()

  def changeActiveSheet(self):
    pass

  def addSheet(self):
    system('cls')
    option = int(input("(1) Manual - (2) Automatic: "))
    if(option == 1 or option == "manual"):
      sheet_name = input("Choose a sheet name: ")
      wb.create_sheet(sheet_name)
      wb.save(os.getenv('FILE_PATH'))
      time.sleep(.2)
      print("Succesfully added: {}".format(sheet_name))
      print()

    elif(option == 2 or option == "automatic"):
      months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Oktober", "November", "December"]
      added = []
      for month in months:
        if month not in wb.sheetnames:
          added.append(month)
          wb.create_sheet(month)
      wb.save(os.getenv('FILE_PATH'))
      time.sleep(.2)
      print("Succesfully added: {}".format(added))
      print()
    else:
      system('cls')
      self.menu()

    self.menu()

  def changeSheet(self):
    pass

  def removeSheet(self):
    pass

  def back(self):
    from main import main_menu
    main_menu()

  def menu(self):
    from main import create_menu, menu_title
    menu_title("Tab Menu", "bright_blue")
    tab_menu = [self.showSheets, self.addSheet, self.changeSheet, self.removeSheet, self.back]

    create_menu(tab_menu)
    