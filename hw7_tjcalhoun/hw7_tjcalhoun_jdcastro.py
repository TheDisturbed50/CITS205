# Thomas Calhoun & Jose Castro
# homework #7
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 25 Feb 2016 to 03 Mar 2016
# Python 3.5.1

'''
#Assignment Details from BLACKBOARD
...Remaining tasks in this assignment:

    Continuing in this file:
        Make a dictionary called plain with the key-value pairs:
        a, 1
        b, 2
        c, 3
        and print it.

        Make an OrderedDict called fancy from the same pairs listed in the step above and print it.
        Print a statement testifying to whether or not it stayed in the same order.

        Make a defaultdict called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and
        append the value 'something for a' to it in one assignment. Print dict_of_lists['a']

        Compress the two files as a .zip (please no .rar or 7z or other weird files thank you so much :D
'''

from newmods import menugen, zoo, goat, guess, age #imported Modules names are small enough, no alias needed.
from collections import OrderedDict, defaultdict
import pprint

spacer = ("+="*39)+"\n" # a fancy effect for the main menu

def assignment_stuffs(): #for the defaultdict part of the assignment...
    print("A heads up, if you skipped option \"2\", you will be sadly disappointed by this section.\n"
          "But no worries, following this section will be another opportunity!\n")
    userMenu = OrderedDict(menugen.menu)
    print("This section is iterating the modifiable diction you constructed in menu option\n"
          "number \"2\", called {}. You may notice the sort by keys (item name).".format(menugen.mTitle))
    print("\n", userMenu, "\n")
    input("Press the ENTER key to continue...".center(80))

    dict_of_lists = defaultdict(list)

    print("Behold, the Dict of Lists...\n",dict_of_lists, "\n (Yes, its empty... I know.)")
    dict_of_lists["a"]
    print("\nAnd now, with a defaultdict assignment...\n",dict_of_lists,"\n")
    print("Now, for this last part of the assignment, I will ask for\n some participation in the audience (you).\n")

    while True:
        print("\n\n")
        askUserAppend = input("Please type a value to insert for key \"a\" in the defaultdict\n"
                              "(Spaces not tolerated within entry)... VALUE: ")
        print("\n")
        dict_of_lists["a"].append(askUserAppend)
        print("This will be displayed in a KEY : VALUE pair:".center(40))
        pprint.pprint(dict_of_lists,indent=4,  width=1)
        print("\n")
        askUserCont = input("Continue? [ Y / N ]:".center(80)).lower()
        if askUserCont == "n":
            return False


def home_menu():
    """
    Main Menu of the program.
    :return:
    """
    while True:
        print("<><>-<><> MAIN MENU <><>-<><>".center(80), "\n", '''
{}+=  [1] See the Zoo Hours!                                                  +=
{}+=  [2] Create a Fun Menu!                                                  +=
{}+=  [3] Test your skills with the Fallout 3 G.O.A.T.!                       +=
{}+=  [4] Play "Guess the Number"!                                            +=
{}+=  [5] See how long you have existed with the Age Calculator!              +=
{}+=  [6] Enough of this Tom-Foolery, get on with the assignment!             +=
{}+=  [Q] Quit Program                                                        +=
{}
        '''.format(spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer)) #printed independently to format easier
        userOption = input("Selection: ") #user input
        if userOption == "1":
            print("\n"*1)
            zoo.hours()
            print("\n"*5)
        elif userOption == "2":
            print("\n"*1)
            menugen.mainMenu()
            print("\n"*5)
        elif userOption == "3":
            print("\n"*1)
            goat.start_goat()
            print("\n"*5)
        elif userOption == "4":
            print("\n"*1)
            guess.call_to_start()
            print("\n"*5)
        elif userOption == "5":
            print("\n"*1)
            age.age_calc()
            print("\n"*5)
        elif userOption == "6":
            print("\n"*1)
            assignment_stuffs()
            print("\n"*5)
        elif userOption in ("q","Q"):
            return False
        else:
            print("I'm sorry, you have entered an option that is not supported. Please select a response\n"
                  "from above, only typing what is listed in the [brackets].\n\n\n\n\n")

home_menu()
