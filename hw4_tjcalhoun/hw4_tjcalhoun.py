# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu 04 Feb 2016
# Python 3.5.1

import sys

print("Welcome to The Command-Prompt Menu Generator!".center(80))

menu = {}
menuItem = None
menuPrice = None

print("Instructions: Type into the input fields and press enter. \nIt will prompt you at each completed entry if you"
      "are finished, or need to add more.\n\n")

finText = "\n\nFinished (Y/N)?:" #String Variables to print during the entry process...
notFinResp = "\nNext Item...\n"

#I like using defined functions, breaking into phases each stage of the program, with the option for callback.

def mainMenu(): #The Nerve center of this application, to direct the user to his/her area of choice.
    while (True):
        global menu #This makes my variable reachable within the function.
        print("--== MAIN MENU ==--".center(80))
        chgDictSelect = input("\nPlease choose from the following menu options:\n[A] Create/Modify Entries\n"
                              "[B] Print all Entries\n[C] Delete an Entry\n[X] Quit Program\n>>> SELECTION:")
        if chgDictSelect in ("a","A"):
            setMenuDict() #call to the function defined below to add keys
        elif chgDictSelect in ("b","B"):
            printAllDict() #call to the function below to print my pretty table.
        elif chgDictSelect in ("c","C"):
            delKeyName = input("\nType the name of the key to delete:\n") #Key deletion, small enough to just perform
            try:                                                          #   within the main menu
                del menu[delKeyName]
            except KeyError:
                pass
            print("Key successfully removed!")
        elif chgDictSelect in ("x","X"):
            sys.exit() #Using the imported "sys" module, this kills the entire script's process.
        else:
            print("\nOops, that option is not available, please try again!\n") #To let the user know if they keyed in
    return True                                                                #   a non-existent option.

def setMenuDict(): #Process for Adding/Modifying Keys
    while (True):
        print("Begin!".center(80))
        menuItem = input("Menu Item:\n") #These empty variables take the user input as strings,
        menuPrice = input("Menu Price:\n")
        menu[menuItem] = menuPrice #and this merges our strings into the dictionary's variable.
        finQuest = input(finText)
        if finQuest in ("y","Y"): #A prompt on whether or not the user would like to continue.
            break
        elif finQuest in ("n","N"):
            print(notFinResp.center(80))
    return True

def printAllDict(): #Process for printing values in a fancy table format
    spacer = ("\n ::"+",:'':,"*10+"::\n")
    spGrid = "::"
    ctrGrid = "--==--"
    rpGrid = "  ::"
    print("\nItems below listed in a 'KEY - VALUE' Pair...",)
    for key,val in menu.items():
        print(spacer, '{0:3s}{1:20s}{2:27s}{3:10s}{4:4s}'.format(spGrid, key, ctrGrid.center(22),
                                                                 val.rjust(10), rpGrid), spacer)

mainMenu()

print("\n\n**Have a great day! Thank you for using The Command-Prompt Menu Generator!**")