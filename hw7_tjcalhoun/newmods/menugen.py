# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 04 Feb 2016 to 10 Feb 2016
# Python 3.5.1
"""
Modified for Module use
"""

import sys

mTitle = ""
menu = {}
menuItem = None
menuPrice = None

finText = "\n\nFinished (Y/N)?:"  # String Variables to print during the entry process...
notFinResp = "\nNext Item...\n"

# I like using defined functions, breaking into phases each stage of the program, with the option for callback.


def mainMenu():  # The Nerve center of this application, to direct the user to his/her area of choice.
    print("Welcome to The Command-Prompt Menu Generator!".center(80))
    print("\nInstructions: Type into the input fields and press enter. \n"
          "It will prompt you at each completed entry if you are finished, or need to add more.\n\n")
    print("--== MENU ==--".center(80))
    while (True):
        global menu, mTitle  # This makes my variable reachable within the function.
        chgDictSelect = input("\nPlease choose from the following menu options:\n"
                              "[T] Assign a Title to your Menu!\n[C] Create/Modify Entries\n"
                              "[P] Print all Entries\n[D] Delete an Entry\n\n[Q] Quit Program\n\n"
                              "[E] Exit Script (Return to Main Menu)\n>>> SELECTION:")
        if chgDictSelect in ("t","T"):
            mTitle = input("Type your new title name, then press the ENTER key:\n")
            print("\n\n","Title Saved Successfully!".center(80),"\n\n")
        elif chgDictSelect in ("c","C"):
            setMenuDict()  # call to the function defined below to add keys
        elif chgDictSelect in ("p","P"):
            printAllDict()  # call to the function below to print my pretty table.
        elif chgDictSelect in ("d","D"):
            delKeyName = input("\nType the name of the key to delete:\n")  # Key deletion, small enough to just perform
            try:                                                           # within the main menu
                del menu[delKeyName]
            except KeyError:
                pass
            print("Key successfully removed!")
        elif chgDictSelect in ("e","E"):
            print("\n\n**Have a great day! Thank you for using The Command-Prompt Menu Generator!**")
            return False #Finishes the loop.
        elif chgDictSelect in ("q","Q"):
            sys.exit() #Using the imported "sys" module, this kills the entire script's process.
        else:
            print("\nOops, that option is not available, please try again!\n")  # To let the user know if they keyed in
    return True                                                                 # a non-existent option.


def setMenuDict():  # Process for Adding/Modifying Keys
    while (True):
        print("Begin!".center(80))
        menuItem = input("Menu Item:\n")  # These empty variables take the user input as strings,
        menuPrice = input("Menu Price:\n")
        menu[menuItem] = menuPrice  # and this merges our strings into the dictionary's variable.
        finQuest = input(finText)
        if finQuest in ("y","Y"):  # A prompt on whether or not the user would like to continue.
            break
        elif finQuest in ("n","N"):
            print(notFinResp.center(80))
    return True


def printAllDict():  # Process for printing values in a fancy table format
    spacer = ("\n ::"+",:'':,"*10+"::\n")
    spGrid = "::"
    ctrGrid = "--==--"
    rpGrid = "  ::"
    print("\nItems below listed in a 'KEY - VALUE' Pair...\n",mTitle.center(80))
    for key,val in menu.items():
        print(spacer, '{0:3s}{1:20s}{2:27s}{3:10s}{4:4s}'.format(spGrid, key, ctrGrid.center(22),
                                                                 val.rjust(10), rpGrid), spacer)