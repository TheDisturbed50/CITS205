# Thomas Calhoun
# EXTRA CREDIT
# tjcalhoun@alaska.edu 24 Mar 2016
# Python 3.5.1

from turtle import *
import time

"""
'Turtle Generator'

A basic drawing algorithm that takes specific parameters by the user
to create a unique drawing using the Turtle Module.

The drawing my jump outside of the window boundaries, but all part of the experiment.
The idea is to get the user to try again, and see how much the different parameters affect the
drawing!
"""

# Global variables assignment
brkt = "="*80
directionList = []
distanceList = []


def get_val():
    """
    Define pen movement parameters.
    Saves values to independent lists.
    :return:
    """
    lpCount = 0
    prntCount = 0

    global directionList, distanceList

    print("We are going to create stages for this art project...".center(80))  # The .center() formatting gets scrubbed
    print("I want you to think of 3 values (Dir & Dist).".center(80))  # by a \n newline signal... Which mandates the
    print("(Dir adjustments will be made to the \"Left\" of the last movement)".center(80))  # multiple print lines.
    time.sleep(0.3)

    while True:  # The list to obtain user input for pen movement data.
        print("\n\n"+brkt)  # Some decor for user input areas
        direction = int(input("Think of a 360-degree compass, please enter a numeric value for direction: "))
        distance = int(input("\nThink of our distance measurement as small pixels, between 1-200.\n"
                             "Please enter a numeric value for distance: "))
        # The above ^ statement for 1-200, is really a goal and not a requirement. A conditional would have sufficed to
        # to control the input values, but this is turtle... Why limit the user?
        print(brkt)
        time.sleep(0.3)
        directionList.append(direction)  # List append, since it stores the values in order, this was an easy choice
        distanceList.append(distance)  # for data storage.
        print("\n\n")
        lpCount += 1  # To regulate the loop length, expandable by user.
        prntCount += 1  # A printed count, one that is not reset below for true representation of #/steps on screen.
        print("Stage {} set...".format(prntCount))
        if lpCount == 3:  # Trigger for when we have enough data to move on
            askContinue = input("Continue adding values? ( Y / N ): ").lower()
            if askContinue == "y":  # ...But maybe the user is feeling adventurous!
                lpCount = 2  # Keeps the loop alive, and forces a prompt for each value addition.
            elif askContinue == "n":
                break
            else:
                print("Please answer with a Y (Yes) or N (No).")  # So nobody can go "Steve Harvey" on that question...
                get_val()


def the_fun():  # Goes against the 'page long function' point from this week's lecture, but hey, it works!
    """
    The driving mechanics of the program which establishes the objects
    that our user-defined variables will be joined with.
    """
    print("\n\nThe following values are going to be used to generate a graphic:")
    print("Direction Variants: ", directionList)  # Printing the data to the user
    print("Distance Variants: ", distanceList)
    time.sleep(0.3)

    # The following variables can be static or overwritten if the user so chooses.
    bgColor = "black"
    tColor = "green"
    fColor = "blue"
    tSpeed = 6
    tSize = 1

    promptCustom = input("\nWould you like to customize some graphic properties of the drawing? ( Y / N ): \n").lower()
    if promptCustom == "y":
        # Allow the user to keep it simple, or go deeper into customization.
        print("\n\nFor color selection, please type the name of the color (keep it basic),\n"
              "or research the hex value:\n"
              "Example: #ffffff is the value for \"white\"\n"
              "http://www.colorpicker.com/ is a basic, yet excellent resource.\n\n")

        print(brkt) # The following data input is error handled, including the color error in case you think turtle
        # knows what "baby-diarrhea" is... (It doesn't, sadly.)
        bgColor = input("Select a color for the background: ").lower()  # Adding some good customization.
        tColor = input("\nSelect a color for your lines: ").lower()
        fColor = input("\nSelect a color to Fill between the lines: ").lower()
        tSpeed = int(input("\nChoose the draw speed (1-slowest / 10-fastest): "))
        tSize = int(input("\nChoose the line width (1-thin / 10-super thick): "))
        print(brkt)
        time.sleep(0.3)

    print("\n\n\n")
    print("Lets make this interesting...".center(80))
    print("\n"+brkt)  # To keep this simple, I used a range. Certainly, there is a smarter way, but we'll save that
    # for another day (I gotta leave something to build on!).
    repeaterVar = int(input("Choose how many times you want to see those iterations repeat (1-100): "))
    varianceVar = int(input("\nChoose a small number to throw in a slight direction variance between repeats: "))
    print(brkt+"\n\n")
    time.sleep(0.3)

    # Local variables. Once used, they disappear into the sunset. The ones that got away...
    bobTheTurtle = Turtle()  # Meet Bob.
    pond = Screen()  # And this pond, for the record, is a public pond. No skinny dipping for Bob.
    pond.bgcolor(bgColor)  # The following are properties of the drawing, whether defined by the user or not.
    bobTheTurtle.speed(tSpeed)  # (my new default values make it a little prettier nonetheless)
    bobTheTurtle.pensize(tSize)
    bobTheTurtle.color(tColor, fColor)

    bobTheTurtle.begin_fill()
    print("Note: check for another Python window to see drawing!")  # Yea, it happens. Sneaky windows...
    for i in range(repeaterVar):
        varianceVar += 1  # I added a variance to your variance. BOOM.
        for d, l in zip(directionList, distanceList):  # A google save here, zip it at the 'for' loop!
            bobTheTurtle.left(d)
            bobTheTurtle.forward(l)
        ii = i+1  # To establish a print counter value.
        print("Repeat {} is complete".format(ii))  # To keep things lively in the prompt window.

    bobTheTurtle.hideturtle()
    print("Drawing Complete!".center(80))  # If your wondering "That's it?", and you see this in the prompt, yes. It is.
    bobTheTurtle.end_fill()  # Colortime!

    # One last turtle definition, to mark within the window for completion.
    fin = Turtle()
    fin.hideturtle()  # Keeps an arrow from showing, since this used solely for text.
    fin.pencolor("yellow")
    fin.penup()  # Learned to do this...
    fin.goto(-125, -375)  # ...BEFORE this.
    fin.write ('Click anywhere in this window to continue...', font = ('Times New Roman', 12))
    pond.exitonclick()  # It's some kind of magic!



def main(*args):  # The cogs of this program, 'Get' - 'Run' - 'Repeat'.
    try:  # A call-all for errors, using the .format to my advantage to let the user know where the boo-boo is.
        # Although, turtle is exception prone I have noticed, so this is a wide net to catch them.
        get_val()
    except Exception as err:
        print("---Oops! an error has occurred:\n"
              "---{}\n"
              "---Please verify your input and try again!\n".format(err))
        get_val()

    try:  # This handler a little more justified, since protecting multiple data types.
        the_fun()
    except Exception as err:
        print("---Oops! an error has occurred:\n"
              "---{}\n"
              "---Please verify your input and try again!\n".format(err))
        the_fun()

main()  # Call to start main program

time.sleep(0.3) # And the closing scene... Fin.
print("\n\n", "Thanks for playing!".center(80),
      "\n",
      "Maybe we'll have a version 2.0 before the end of the semester!".center(80), "\n\n\n\n")
input("Press enter to exit...".center(80))

"""
Footnote:
A retry function was intended, but removed to due poor compatibility.

It was throwing an error for reinstating the Turtle window, so I would have had to overhaul 'the_fun()'
function to work with pond.mainloop() and maybe pond.onclick() to workaround another error experienced with
pond.exitonclick().

To complete this assignment timely, I settled for a little less flair.
"""