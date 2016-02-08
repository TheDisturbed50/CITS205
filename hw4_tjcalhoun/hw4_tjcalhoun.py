# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu 04 Feb 2016
# Python 3.5.1


#Your application must:
#    run without errors or exceptions
#    ask for data in a clear and concise manner
#    be able to collect data until the user says they're done
#    sort the collected data and the extrapolated data in a tidy and attractive table
#    apply an algorithm that works for all reasonable input (outlier cases are exceptions)
#    while loop to gather data
#To get full credit, you must:
#    use good python style (including 80 char width maximum)
#    comment your code
#    challenge yourself!
#Freebies, this time!
#    assume good data
#    no error checking necessary
#Hints:
#    a while loop is a great way to build your collection of data
#    a list or a dictionary is a great way to store your data
#    make sure you can enter 10 different items and your algorithm works for all of them!

print("Welcome to The Command-Prompt Menu Generator!")

menu = {"Sammich":"$2", "Fries":"$1", "Pop":"$0.75"}
menuItem = None
menuPrice = None

input("\n\nPress enter to begin\n\n")
print("Instructions: Type into the input fields and press enter. \nIt will prompt you at each completed entry if you"
      "are finished, or need to add more.\n\n")
finText = "\n\nFinished (Y/N)?\n"
notFinResp = "\n\nNext Item...\n"

#def setMenuDict():
#    while (True):
#        print("Begin!\n\n")
#        menuItem = input("Menu Item:\n")
#        menuPrice = input("Menu Price:\n")
#        menu[menuItem] = menuPrice
#        finQuest = input(finText)
#        if finQuest in ("y","Y"):
#            break
#        else:
#            print(notFinResp)
#    return True

#menuStr = list(menu)

def printAllDict():
    while (True):
        printResult = input("\nWould you like to review your entries? (Y/N):\n")
        if printResult in ("n","N"):
            break
        elif printResult in ("y","Y"):
            spacer = ("\n"+"~**~"*15+"\n")
            print(spacer,"\nItems below listed in a 'KEY - VALUE' Pair...",)
            for key,val in menu.items():
                print(spacer, '{0:28}-=-                     {1:10}'.format(key, val), spacer)

def dictEntryProcess():
    print("\n\nLets create a Menu!\n\n")
    #setMenuDict()
    printAllDict()

def lastChance():
    questionOfTheCentury = input("\n\nDo you want to make any modifications to those Menus? (Y/N):\n")
    while (True):
        if questionOfTheCentury in ("n","N"):
            break
        elif questionOfTheCentury in ("y","Y"):
            chgDictSelect = input("\nPlease select Menu you would like to change ([x] to Cancel) :"
                                  "\n[A] Menu\n>>> SELECTION:   \n\n")
            if chgDictSelect in ("a","A"):
                setMenuDict()
            elif chgDictSelect in ("x","X"):
                break

dictEntryProcess()
lastChance()
