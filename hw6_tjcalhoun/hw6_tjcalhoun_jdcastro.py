# Thomas Calhoun & Jose Castro
# homework #6
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 18 Feb 2016 to 25 Feb 2016
# Python 3.5.1

from random import randint

random = randint(1, 21)

# The Welcome Screen

print("Welcome to the number guessing game!")
print()
Userinput = input("Please tell me your name: ")
Useroutput = str(Userinput)



print()
print("\n")
print("I am thinking of a number between 1 and 20" )
print()
print("Can you guess it?")

print("\n")

num = int(input("Enter a number between [1-20]: "))

def guess_loop():
    global num
    while num != random:

        if num > 20:
            print("\nError_00: You entered a number that exceeds the possible guess bounds...\n"
                  "    Please re-enter your guess and try again.\n")
            num = int(input("Enter a number [1-20]: "))
            continue

        elif num > random:

            print ("Too High")
            num = int(input("Enter a number [1-20]: "))
            continue

        elif num < random:
            print ("Too Low")
            num = int(input("Enter a number [1-20]: "))
            continue



try:
    guess_loop()
except ValueError as err:
    print("Error_01: Wrong input! You need to type a number. Please re-enter and try again.")
    guess_loop()
except Exception as err:
    print("Error_02: Unknown Exception raised, please re-check value entered and try again!")
    guess_loop()

# The Correct Guess

print("\n")
print("Congratulations YOU WIN!!!")
print()
print("Thank you " + Useroutput + " for your participation!")
print("\n")
input("Press RETURN to exit..")