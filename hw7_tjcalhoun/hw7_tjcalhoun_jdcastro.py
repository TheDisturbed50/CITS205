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

from newmods import menugen, zoo, goat, guess, age

spacer = ("+="*40)+"\n"

def assignment_stuffs(): #for the defaultdict part of the assignment...
    print("//   // UNDER CONSTRUCTION //   //".center(80)) #placeholder
    print("//   // UNDER CONSTRUCTION //   //".center(80))
    print("//   // UNDER CONSTRUCTION //   //".center(80))

def home_menu():
    """
    Main Menu of the program.
    :return:
    """
    while True:
        print("<><>-<><> MAIN MENU <><>-<><>".center(80), "\n", '''
{}+=  [1] See the Zoo Hours!                                                    +=
{}+=  [2] Create a Fun Menu!                                                    +=
{}+=  [3] Test your skills with the Fallout 3 G.O.A.T.!                         +=
{}+=  [4] Play "Guess the Number"!                                              +=
{}+=  [5] See how long you have existed with the Age Calculator!                +=
{}+=  [6] Enough of this Tom-Foolery, get on with the assignment!               +=
{}+=  [Q] Quit Program                                                          +=
{}
        '''.format(spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer))
        userOption = input("Selection: ")
        if userOption == "1":
            print("\n"*10)
            zoo.hours()
            print("\n"*5)
        elif userOption == "2":
            print("\n"*10)
            menugen.mainMenu()
            print("\n"*5)
        elif userOption == "3":
            print("\n"*10)
            goat.start_goat()
            print("\n"*5)
        elif userOption == "4":
            print("\n"*10)
            guess.call_to_start()
            print("\n"*5)
        elif userOption == "5":
            print("\n"*10)
            age.age_calc()
            print("\n"*5)
        elif userOption == "6":
            print("\n"*10)
            assignment_stuffs()
            print("\n"*5)
        elif userOption in ("q","Q"):
            return False

home_menu()