# Thomas Calhoun & Jose Castro
# homework #6
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 18 Feb 2016 to 25 Feb 2016
# Python 3.5.1

from random import randint

# The Welcome Screen

print("Welcome to the number guessing game!")
print()

#The variable to be reassigned or utilized later
fancySpacer = "*^^*"*15  # A decorative spacer to segregate the sections of this program at a user perspective.
genderVar = ""
random = randint(1, 20)
num = 0 # gets reassigned later in the function

def name_set(): # the First called function, to identify our victim... erm, I mean player. Yeah.
    global Userinput, genderInput, genderVar
    Userinput = input("Please tell me your name: ")
    while True: # a loop was the easiest way to demand a consistent answer from the user.
        genderInput = input("Now, select from one of the following Genders:\n"
                            " 'male'?\n 'female'?\n 'dragon'?\nChoice: ").lower()
        if genderInput == "male":
            genderVar = "Sir "
            break
        if genderInput == "female":
            genderVar = "Madame "
            break
        if genderInput == "dragon": #whoever does not choose this is not worthy... just saying.
            genderVar = "Oh great and Powerful "
            Userinput = "Smaug"
            break
        else: # the 'keep alive' for the loop, no break is ordered if we don't get what we want.
            print("\nOops! Input not recognized! Please type an appropriate gender! (no spaces) \n")

# After the amount of tries is expended.
def losers_weep():
    print("\nI regret to inform you, that you have lost.\n    Better luck next time!!!")
    print()
    print("Thank you, " + genderVar + Useroutput.title() + " for your participation!")

# The Correct Guess
def winner_circle():
    print("\nCongratulations YOU WIN!!!")
    print()
    print("Thank you, " + genderVar + Useroutput.title() + " for your participation!")
    if Useroutput is "Smaug":
        print("\nYou may have noticed that your name has been modified... \n    Only {} is a truly notable name "
              "for a dragon in this realm!\n".format(Useroutput))

def easter_egg():
    print("\n\n\n\n\n<<< EASTER EGG PLACER 'Test'>>>\n\n\n\n") #need to further develop this feature
    input("Test INPUT:  ")

def guess_loop(): # the gears of our game.
    def difficulty_select(): # allows the user to tailor the difficulty to their skills
        global setTries, setMax
        setTries = 0
        setMax = 20
        print(fancySpacer, "\n\nHear ye, hear ye, {}{}, \n    You have a chance to affect your destiny...\n"
              "Choose from one of the following difficulties:\n"
              "  [A] I laugh at the face of death, when if comes to guessing... \n"
              "      (3 Tries, 25 Possibilities)\n" # inspired by Thomas' wife. Since she had a winning streak... -.-
              "  [B] I guess I could guess as good as the rest... \n"
              "      (7 Tries, 20 Possibilities)\n"
              "  [C] Guessing is for losers... \n"
              "      (10 Tries, 20 Possibilities)\n".format(genderVar,Useroutput.title()))
        diffSelect = input("Your Choice: ").lower()
        if diffSelect == "a":
            setTries = 3
            setMax = 25
        if diffSelect == "b":
            setTries = 7
            setMax = 20
        if diffSelect == "c":
            setTries = 10
            setMax = 20
    difficulty_select() # calling the above function to set the difficulty
    global num
    tries = setTries # num of tries set by our difficulty.
    print(fancySpacer+"\n")
    print("I am thinking of a number between 1 and %i" % setMax)
    print()
    print("Can you guess it in %i attempts?!\n" % tries)
    num = int(input("Enter a number [1-{}]: ".format(setMax)))
    numList = [] #easter egg step 1: list to log input
    eEggQuota = [2,0,5] #easter egg step 2: a criteria to meet to enable easter egg
    while tries > 0: # active loop
        tries -= 1 # deduction per iteration.
        numList.append(num)
        print("You have %s tries remaining!" % tries) # a nice reminder, but it also prints after a matching guess...
        if numList == eEggQuota: #activation of easter egg!
            easter_egg()
        elif num != random:
            if num > setMax:
                print("\nError_00: You entered a number that exceeds the possible guess bounds...\n"
                      "    Please re-enter your guess and try again.\n") # basic error check
                num = int(input("Enter a number [1-{}]: ".format(setMax)))
                continue
            elif tries == 0: # our losing factor
                losers_weep()
                break
            elif num > random:
                print ("Too High, guess again!\n")
                num = int(input("Enter a number [1-{}]: ".format(setMax)))
                continue
            elif num < random:
                print ("Too Low, guess again!\n")
                num = int(input("Enter a number [1-{}]: ".format(setMax)))
                continue
        elif num == random: # our winning factor.
            winner_circle()
            break

name_set() # Call to begin the program.

Useroutput = str(Userinput)

try: # Call to begin the game with exception handling.
    guess_loop()
except ValueError as err:
    print("Error_01: Wrong input! You need to type a number. Please re-enter and try again.")
    guess_loop()
except Exception as err:
    print("Error_02: Unknown Exception raised, please re-check value entered and try again!")
    guess_loop()

print("\n")
input("Press RETURN to exit..")