# Written by Thomas John Calhoun
# Jan 15 2016, Py 3.5.1
# Personal Milestone: My first Python program! (After my week1 Python class experience)
"""
Modified for Module use
"""

import datetime

def age_calc():  # Error handling function
    """
    Age Calculator: Input the month, day, and year of someone (or something),
       and then see a value that lists the age of said item/person.
    :return:
    """
    try:
        calc_run()
    except Exception as err:
        print("Oooooops! {} Happened!".format(err))
        print("\nPlease verify you entered good data, and try again!")
        age_calc()  # I do this so that I am 100% sure errors will be handled after an initial exception.


def calc_run():
    print("Welcome to the Fabulous Age Checker!".center(80))
    print()

    YEAR = datetime.date.today().year  # Breaking down the date into segments allows me to have it...
    MONTH = datetime.date.today().month  # ...printed in any order I like.
    DAY = datetime.date.today().day
    print("\nCurrent date: %d/%d/%d" % (MONTH, DAY, YEAR))  # ...Since M/D/Y is the American way, 'MURICA!

    print("\n\n")
    BMONTH = int(input("Birth month? MM  ->"))  # User Birthday input
    BDAY = int(input("Day of birth? DD ->"))
    BYEAR = int(input("Birth year? YYYY ->"))

    TIME = datetime.date.today() - datetime.date(BYEAR, BMONTH, BDAY)  # This shows in DAYS total
    Y,D = divmod(TIME.days, 365)  # divides by years
    AGE = TIME.days  # Discovery: .days prevents a timestamp of zeros from showing.

    print()
    print('And now, The moment of truth! Here is the breakdown of your time in existence...')
    print("{} Years, {} Days.".format(Y,D))
    print(AGE," Days Total.")
    print()

    input("\nPRESS ENTER TO CLOSE")