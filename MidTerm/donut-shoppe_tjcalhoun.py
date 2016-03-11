# Thomas Calhoun &
# MIDTERM
# tjcalhoun@alaska.edu 10 Mar 2016
# Python 3.5.1
# MidTerm Question # 21, good curve ball! (Its a good thing I have a passion for donuts!) (Missed the 2hr deadline)
# ...And missed that deadline from writing this by like 10 minutes! But at least I get to so some fluff
#    before the next retry. (Spent about an extra hour to beef this up. I don't want a boring donut shop!)

# I'm going to leave the following docstring, as it keeps me on track on some of these lessons!
"""
Consider the following scenario:

Your job is to program a digital ordering sign!

A donut shoppe sells donuts for $1.00 each, unless you buy 12 or more. If you buy 12 or more,
the donuts are .75 cents each. (2 points for correct math!)

The program must greet the customer and ask how many donuts they want, and then return the price
and ask them to pull forward. (2 points for inputs and outputs - spelling and punctuation count!)

Don't let them enter negative numbers, zero, or letters! Donuts are serious business! Nobody has
time for that nonsense. (3 points for error checking)

Use IDLE or whatever program you like to write *.py files in and upload it here! (2 points if it runs)
"""

import time, pprint

# Our global variables
regOrder = {}
filOrder = {}
barOrder = {}
genderDeclared = ""
currSelection = ""
donutCount = 0
lessCost = 1.0
moreCost = 0.75


def reg_donuts():  # These first 3 functions define our product lines, allow the user to add to cart.
    """
    Shopping Area 0
    Plain, Round, Hole-ey.
    :return:
    """
    global regOrder, donutCount, currSelection
    currSelection = "Regular Donuts"
    print("Great choice! {} never disappoint!".format(currSelection), "\n\n")
    while True:
        variety = input("Please type the Flavor you seek: ")  # Lets just say we have more options that Baskin Robbins.
        qty = int(input("Quantity Requested: "))  # Forcing this as an INT, to prevent any math errors later on.
        variety = variety.title()  # To make the user's entry more presentable later on.
        regOrder[variety] = qty  # Placing the user's input into a dictionary.
        donutCount += qty  # updating the global Quantity in the process.
        askToCont = input("\n Continue Adding {}? [ Y / N ]".format(currSelection)).lower()
        if askToCont == "n":  # An exit to the input loop.
            break


def filled_donuts():
    """
    Shopping Area 1
    Hole-less, Stuffed with Mystery, and sometimes, Messy.
    :return:
    """
    global filOrder, donutCount, currSelection
    currSelection = "Filled Donuts"
    print("Great choice! {} are the path to true happiness!".format(currSelection), "\n\n")
    while True:
        variety = input("Please type the Flavor you seek: ")
        qty = int(input("Quantity Requested: "))
        variety = variety.title()
        filOrder[variety] = qty
        donutCount += qty
        askToCont = input("\n Continue Adding {}? [ Y / N ]".format(currSelection)).lower()
        if askToCont == "n":
            break


def donut_bars():
    """
    Shopping Area 2
    PERFECTION. Why waste time on anything else, like the pursuit for success and happiness?
    :return:
    """
    global barOrder, donutCount, currSelection
    currSelection = "Donut Bars"
    print("Great choice! {} are often seized in Colombian drug raids!! "
          "So you know they're good!".format(currSelection), "\n\n")
    while True:
        variety = input("Please type the Flavor you seek: ")
        qty = int(input("Quantity Requested: "))
        variety = variety.title()
        barOrder[variety] = qty
        donutCount += qty
        askToCont = input("\n Continue Adding {}? [ Y / N ]".format(currSelection)).lower()
        if askToCont == "n":
            break


def donut_menu():  # The Main menu!
    """
    Main Menu
    Calls to the products for shopping, and also generates the cart information.
    :return:
    """
    cost = 0
    while True:  # The loop to manage menu options, keeps the script alive.
        header = "="*80
        print(header,"\n" , "(o) (o) (o) (o) MAIN - MENU (o) (o) (o) (o)".center(80),"\n"+header, "\n",
              "\n\nPlease select from one the following numerical menu options:\n"
              "    1 - Order some Regular Donuts.\n    2 - Order some Filled Donuts.\n    3 - Order some Donut Bars!\n"
              "\n    9 - VIEW CART\n\n    0 - Exit\n",
              "\n\nSingle Donut Price (Each) .............................. $1.00\n"
              "Dozen & Over, Donut Price (Each) ....................... $0.75\n"
              "(Note, Volume ordering discounts are applied after 12 Donuts added to cart!)\n")
        time.sleep(0.5)
        print(header)
        menuSelect = int(input("SELECTION: "))  # Another forced INT selection
        print(header)
        if menuSelect == 9:  # Shopping Cart, I designed this to serve as a 'print from screen' option before checkout
            print("\n\n\n\n", "SHOPPING CART:".center(80),)
            print("\n\n    Regular Donuts:")  # A clean way to present the dictionaries...
            pprint.pprint(regOrder,indent=4,  width=2)  # And a clean way to view the dictionaries...
            print("\n    Filled Donuts:")
            pprint.pprint(filOrder,indent=4,  width=2)
            print("\n    Donuts Bars:")
            pprint.pprint(barOrder,indent=4,  width=2)
            if donutCount < 12:  # This conditional waits to add in the discount, until last minute before being printed
                cost = lessCost*donutCount
            elif donutCount >= 12:
                cost = moreCost*donutCount
            print("\n  Total Ordered:        ${}".format(donutCount), "\n  Total Due:            ${}".format(cost))
            print("\n\n\n\nPlease press CTRL + P on your keyboard to print this page if your order is "
                  "complete,".center(80),"\n","and present it to the cashier".center(80),
                  "\n\nThank you for shopping with us, {}!".format(genderDeclared), "\n\n\n")
            print("PRESS ENTER WHEN DONE (If you needed to print screen first)".center(80), "\n\n\n")
            input("\n\n\n")  # Screen pause to allow user to control+p the screen if needed.
        elif menuSelect == 1:
            try:  # all other options are error handled, since we use STR input for the quantity.
                reg_donuts()
            except ValueError as err:  # The expected value exceptions, "err" will give a literal view of the error
                print("\n\nUh-Oh! We experienced an error with that value:\n"
                      "{}\n"  # {} with .format() is my best friend in string iteration.
                      "Please Try Again!\n\n".format(err))
            except Exception as err:  # For the unknown out there.... "Aliens".
                print("\n\nUh-Oh! We experienced an error that was unexpected!:\n"
                      "{}\n"
                      "Please Try Again!\n\n".format(err))
        elif menuSelect == 2:
            try:
                filled_donuts()
            except ValueError as err:
                print("\n\nUh-Oh! We experienced an error with that value:\n"
                      "{}\n"
                      "Please Try Again!\n\n".format(err))
            except Exception as err:
                print("\n\nUh-Oh! We experienced an error that was unexpected!:\n"
                      "{}\n"
                      "Please Try Again!\n\n".format(err))
        elif menuSelect == 3:
            try:
                donut_bars()
            except ValueError as err:
                print("\n\nUh-Oh! We experienced an error with that value:\n"
                      "{}\n"
                      "Please Try Again!\n\n".format(err))
            except Exception as err:
                print("\n\nUh-Oh! We experienced an error that was unexpected!:\n"
                      "{}\n"
                      "Please Try Again!\n\n".format(err))
        elif menuSelect == 0:  # Termination of the script.
            break  # "You've been Terminated..."
        else:  # To handle an input outside of the menu options (if integer)
            print("\n    I'm sorry! Incorrect value was entered!, please try again!\n\n")


def welcome():  # A warm welcome.
    print("Welcome to the \"Super Awesome Donut Shop\"!".center(80), "\n",
          "Where fun and taste is all that matters!".center(80), "\n",
          "The only thing 'Gluten-Free' is the door...".center(80), "\n\n\n")

    def gender():  # This is nested so it could restart to this point exactly, for the else condition below.
        """
        Gender Selection, for menu output responses.
        :return:
        """
        global genderDeclared  # So that our program can recognise our user from other functions.
        time.sleep(0.5)
        print("Now, how can we help you? Sir or Ma'am?")
        time.sleep(0.3)
        gender_ask = input("\n    Are you:\n    [A]: Male?\n    [B]: Female?\n\nSELECTION: ").lower()
        if gender_ask == "a":  # "Classy".
            genderDeclared = "Sir"
        elif gender_ask == "b":
            genderDeclared = "Ma'am"
        else:
            print("\n    I'm sorry! Incorrect value was entered!, please try again!\n\n")
            time.sleep(0.3)
            gender()

        print("\nAh, very good! Nice to meet you, {}!\n\n\n".format(genderDeclared))
        try:  # And here, the great error handler to catch all voodoo beyond the gender selection / greeting.
            donut_menu()  # The ABOVE handlers proved not to be redundant through testing, as they protect the dicts val
        except ValueError as err:
            print("\n\nUh-Oh! We experienced an error with that value you entered:\n"
                  "{}\n"
                  "Please verify your input, and Try Again!\n\n".format(err))
            donut_menu()  # Testing showed that this was needed to keep the program running (not in loop when called).
        except Exception as err:
            print("\n\nUh-Oh! We experienced an error that was unexpected!:\n"
                  "{}\n"
                  "Please verify your input, and Try Again!\n\n".format(err))
            donut_menu()

    try:  # Calling the nested function, running a handler just in case (I was never able to generate an exception)
        gender()
    except Exception as err:
        print("\n\nUh-Oh! We experienced an error that was unexpected!:\n"
              "{}\n"
              "Please verify your input, and Try Again!\n\n".format(err))
        gender()

welcome() # and the line that starts it all!

print("Thank you again {}, we really appreciate your business!!!".format(genderDeclared))