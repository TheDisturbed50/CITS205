# Thomas Calhoun
# SIDE PROJECT
# tjcalhoun@alaska.edu 29 Mar 2016
# Python 3.5.1

import pandas as pd
from urllib.request import urlopen

prnt = "\n\nNOTE:\nIf the program returns an empty list, then the name you searched is not record\n" \
       "with selected Detachment.\n\n"
link = "http://www.dps.state.ak.us/ast/warrants/ASTActiveWarrantsToPublish.csv"


def warrant_checker(search, altSearch):
    warrReq = urlopen(link)

    warrants = pd.read_csv(warrReq, encoding="utf-8-sig")
    warrFilt1 = warrants.loc[(warrants["Detachment"] == search)]
    warrFilt2 = warrFilt1.loc[(warrants["person_name_last"] == altSearch)]
    warrFiltClean = warrFilt2.drop(warrFilt2.columns[[0, 1, 10, 11]], axis=1)
    warrFiltered = warrFiltClean.to_string()

    print(warrFiltered)


def main():
    while True:
        print("<<< MAIN MENU >>>".center(80))
        print('''
          === ALASKA STATE TROOPERS ===
          ===    ACTIVE WARRANTS    ===

        Please choose from the following:

        1 - Trooper Detachment A (Ketchikan)
        2 - Trooper Detachment B (Palmer)
        3 - Trooper Detachment C (Anchorage)
        4 - Trooper Detachment D (Fairbanks)
        5 - Trooper Detachment E (Soldotna)
        6 - ABI Trooper Detachment
        7 - Search all

        0 - Exit

        ''')
        ask = int(input("Choice: "))
        if ask == 0:
            break
        elif ask == 1:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("A Detachment", alt)
        elif ask == 2:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("B Detachment", alt)
        elif ask == 3:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("C Detachment", alt)
        elif ask == 4:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("D Detachment", alt)
        elif ask == 5:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("E Detachment", alt)
        elif ask == 6:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("H Detachment", alt)
        elif ask == 7:
            print("Looking for someone? Search for them here! (Last Name) ")
            print(prnt)
            alt = input("(Leave blank to view entire record)\n    INPUT: ").capitalize()
            warrant_checker("", alt)
        else:
            print("\n\nInput not recognized, please enter one of the menu options.\n\n")

if __name__ == '__main__':
    while True:
        try:
            main()
        except ValueError:
            print("Woops, input value must be a number! Try again!")
