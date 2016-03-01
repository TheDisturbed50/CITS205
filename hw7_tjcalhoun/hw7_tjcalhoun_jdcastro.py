# Thomas Calhoun & Jose Castro
# homework #7
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 25 Feb 2016 to 03 Mar 2016
# Python 3.5.1

'''  #Assignment Details from BLACKBOARD
Want to take creative license with it and make it your own?
Go for it!
Don't go too crazy, though - we've got our midterm on the 9th, and this is your last homework before Spring Break!

    Create a file called zoo.py. In it, define a function called hours() that prints the string 'Open 9-5 Daily'.

    Create a second file named after you! Like this: hw5_jmokinczy.py. In this file, import the zoo module as menagerie and call its hours() function.

    Continuing in this file:
        Make a dictionary called plain with the key-value pairs:
        a, 1
        b, 2
        c, 3
        and print it.

        Make an OrderedDict called fancy from the same pairs listed in the step above and print it.
        Print a statement testifying to whether or not it stayed in the same order.

        Make a defaultdict called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a']

        Compress the two files as a .zip (please no .rar or 7z or other weird files thank you so much :D
'''

from newmods import menugen

menugen.mainMenu()