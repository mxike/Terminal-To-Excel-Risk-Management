class Tab:
  def addTab(self):
    print("add Tab")

  def back(self):
    from main import main_menu
    main_menu()

  def menu(self):
    from main import create_menu
    tab_menu = [self.addTab, self.back]

    create_menu(tab_menu)
    