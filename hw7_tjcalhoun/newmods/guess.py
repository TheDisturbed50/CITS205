# Thomas Calhoun & Jose Castro
# homework #6
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 18 Feb 2016 to 25 Feb 2016
# Python 3.5.1

"""
Modified for Module use
"""

from random import randint
import time

#The variables to be reassigned or utilized later
fancySpacer = "*^^*"*15  # A decorative spacer to segregate the sections of this program at a user perspective.
genderVar = ""
Userinput = ""
random = 0
num = 0 # gets reassigned later in the function

def name_set(): # the First called function, to identify our victim... erm, I mean player. Yeah.
    global Userinput, genderInput, genderVar
    Userinput = input("Please tell me your name: ")
    print()
    while True: # a loop was the easiest way to demand a consistent answer from the user.
        genderInput = input("Now, select from one of the following Genders:\n\n"
                            " Male\n Female\n Dragon \n\nChoice: ").lower()
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

def easter_egg(): # an extra element to add to the fun
    print("WARNING".center(80))
    time.sleep(3.00)
    print()
    print("WARNING".center(80))
    time.sleep(3.00)
    print()
    print("WHAT DID YOU DO".center(80))
    time.sleep(3.00)
    print()
    print("DO YOU KNOW WHAT YOU JUST DID!!!".center(80))
    time.sleep(3.00)
    print()
    print("IT TOOK US A WHILE TO LOCK HIM UP".center(80))
    print()
    time.sleep(3.00)
    print()
    print("\n\n\n\n\n"+"LOOK WHAT YOU HAVE YOU DONE!!!!!!".center(80)+"\n\n\n\n")
    time.sleep(3.00)
    input("""


           .'''*(7????(C?!!,''.                                           
           '!(7(!,,!?,,,,!!,,!!C!!,       
        '!(?,,,?,,,,,,,,,,,,,,,(,,!7!'      
       !?((,,,,,,,,,,,,,,,,,,,,,,,,*C??        
     ?=*,,,,,?!!,,,,,,,,,,,,,,,,,,,,,,,=*                                   
   .?((,,,,*?((=C=!,,,,,,,,,,,,,,,,,**,((*    
 .*=!,,,,,?!.    *(*,,,,,,,,,,,,*(=77(!,,?*   
 ==?,,,,,,(   ?   .=,,,,,,,,,,,*(*'''!?,,,C.    
 ===,,,,,,(  .,.. .7,,,,,,!?,,,=   ', '(,,??   You Have Released Me 
   '(*,,,,(C=?!!?7C*,,,,,,*7,,*=,,,,,  =,,,(=,    VICTORY WILL BE MINE
    '??,,,,!?(?((!*,,,,,,,*=,,,7(!!*!?=!,,(7=,                              
      ,?!,,,,,,,,,,,,,,,,?33*,,,?(???(**??.                                 
        '!?**,,,,,,,,,,,,,**,,,,,,,*,*?!'                                   
         .*=7(?*,,,,,,,,,,,,,,,,,,!(!!.                                     
 ,!!*'????!****?73C?!**!??***!?(((!((?!''.'.                                
 C=**!(=,,,,,,,,=A5????=A5???!*,,,,,,,*=7!*!?                               
*(((*,,=!,,,,***C35!***(55=,,,,,,,,,,,(??*,77.                              
=*C7!,,==??CJ3%$$=A$$$$A=33????????((?C,*?=7?(                              
'=?C!(*.  'AA%%%%%%%%%%%%A3          .!?*7=(7'                              
 .',,.    7%%%%%%%%%%%%%%%%            '*!*'.                               
         .A%%%%%%%%%%%%%%%%                                                 
         ?A%%%%%%%AA55A%%%A'                                                
         C%%%%%%%%#A%%%%%%%7          

Press enter to spank Stewie for being a cranky butt and set him in his crib for a nap...
          """+"\n"+"ACHIEVEMENT UNLOCKED:".center(80)+"\n"+
          "Bedtime will be mine!".center(80)+"\n\n\nPress enter to continue...")

def easter_egg2():
    print("\n\n\n\n\n"+"ALASKANIZED!!!".center(80)+"\n\n\n\n")
    input("""


                                            .      //
                                       /) \ |\    //
                                 (\\\\|  || \)u|   |F     /)
                                  \```.FF  \  \  |J   .'/
                               __  `.  `|   \  `-'J .'.'
        ______           __.--'  `-. \_ J    >.   `'.'   .
    _.-'      ""`-------'           `-.`.`. / )>.  /.' .<'
  .'                                   `-._>--' )\ `--''
  F .                                          ('.--'"
 (_/                                            '\\
  \                                             'o`.
  |\                                                `.
  J \          |              /      |                \\
   L \                       J       (             .  |
   J  \      .               F        _.--'`._  /`. \_)
    F  `.    |                       /        ""   "'
    F   /\   |_          ___|   `-_.'
   /   /  F  J `--.___.-'   F  - /
  /    F  |   L            J    /|
 (_   F   |   L            F  .'||
  L  F    |   |           |  /J  |
  | J     `.  |           | J  | |              ____.---.__
  |_|______ \  L          | F__|_|___.---------'
--'        `-`--`--.___.-'-'---

    """+"\n"+"ACHIEVEMENT UNLOCKED:".center(80)+"\n"+"Alaskan Curiosity!".center(80)+"\n\n\nPress enter to continue...")

def guess_loop(): # the gears of our game.
    global random, num
    def difficulty_select(): # allows the user to tailor the difficulty to their skills
        global setTries, setMax, random, num
        setTries = 0
        setMax = 20
        print(fancySpacer, "\n\nHear ye, hear ye, {}{}, \n    You have a chance to choose your destiny...\n"
              "\n"
              "Choose from one of the following difficulties:\n"
              "\n"
              "  [A] I laugh at the face of death, when if comes to guessing... \n"
              "      (3 Tries, 30 Possibilities)\n" # inspired by Thomas' wife. Since she had a winning streak... -.-
              "  [B] I guess I could guess as good as the rest... \n"
              "      (7 Tries, 25 Possibilities)\n"
              "  [C] Guessing is for losers... \n"
              "      (10 Tries, 20 Possibilities)\n".format(genderVar,Userinput.title()))
        diffSelect = input("Your Choice: ").lower()
        if diffSelect == "a":
            setTries = 3
            setMax = 30
        if diffSelect == "b":
            setTries = 7
            setMax = 25
        if diffSelect == "c":
            setTries = 10
            setMax = 20
    difficulty_select() # calling the above function to set the difficulty
    tries = setTries # num of tries set by our difficulty.
    random = randint(1, setMax) #the random module is called, and works with a variable assigned.
    print(fancySpacer+"\n")
    print("I am thinking of a number between 1 and %i" % setMax)
    print()
    print("Can you guess it in %i attempts?!\n" % tries)
    num = int(input("Enter a number [1-{}]: ".format(setMax)))
    numList = [] #easter egg step 1: list to log input
    cits205 = [2,0,5] #easter egg step 2: a criteria to meet to enable easter egg
    akPride = [9,0,7]
    numBufferHigh = [] #using these empty lists to append below
    numBufferLow = []
    for increase in range(random+1,random+6): # the following loops will help guide our victim-player to success!
        numBufferHigh.append(increase)
    for decrease in range(random-6,random):
        numBufferLow.append(decrease)
    while tries > 0: # active loop
        tries -= 1 # deduction per iteration.
        numList.append(num)
        print("You have %s tries remaining!" % tries) # a nice reminder, but it also prints after a matching guess...
        if numList == cits205: #activation of easter egg!
            easter_egg()
            tries += 2
        elif numList == akPride: #activation of easter egg!
            easter_egg2()
            tries += 2
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
                if num in numBufferHigh:
                    print("But, you are close!")
                num = int(input("Enter a number [1-{}]: ".format(setMax)))
                continue
            elif num < random:
                print ("Too Low, guess again!\n")
                if num in numBufferLow:
                    print("But, you are close!")
                num = int(input("Enter a number [1-{}]: ".format(setMax)))
                continue
        elif num == random: # our winning factor.
            winner_circle()
            break

# After the amount of tries is expended.
def losers_weep():
    print("\nI regret to inform you, that you have lost. "
          "The number was {}!\n    Better luck next time!!!".format(random))
    print()
    print("Thank you, " + genderVar + Userinput.title() + " for your participation!\n")
    print("Would you like to try again?")
    restartPrompt = input("[Y / N]:  ").lower()
    if restartPrompt == "y":
        guess_loop()
    else:
        print("\n\nOkay, Goodbye!\n")

# The Correct Guess
def winner_circle():
    print("\nCongratulations YOU WIN!!! The number was indeed {}!".format(random))
    print()
    print("Thank you, " + genderVar + Userinput.title() + " for your participation!")
    if Userinput is "Smaug":
        print("\nYou may have noticed that your name has been modified... \n    Only {} is a truly notable name "
              "for a dragon in this realm!\n".format(Userinput))

def call_to_start():
    # The Welcome Screen
    print("Welcome to the number guessing game!".center(80))
    print()
    name_set() # Call to begin the program.

    try: # Call to begin the game with exception handling.
        guess_loop()
    except ValueError as err:
        print("Error_01: Wrong input! You need to type a number. Please re-enter and try again.")
        guess_loop()
    except Exception as err:
        print("Error_02: Unknown Exception raised, please re-check value entered and try again!")
        guess_loop()


