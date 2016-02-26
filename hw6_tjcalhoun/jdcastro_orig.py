import random

from random import randint

random = randint(1, 20)

# The Welcome Screen

print("Welcome to the number guessing game!")
print()
Userinput = input("Please tell me your name:")
Useroutput = str(Userinput)
print()

print("\n")
print("I am thinking of a number between 1 and 20" )
print()
print("Can you guess it?")

print("\n")

num = int(input("Enter a number between [1-20]:"))

while num != random:

    if num > random:

        print ("Too High")
        num = int(input("Enter a number [1-20]: "))
        continue

    elif num < random:
        print ("Too Low")
        num = int(input("Enter a number [1-20]: "))
        continue

# The Correct Guess

print("\n")
print("Congratualtions YOU WIN!!!")
print()
print("Thank you " + Useroutput + " for your participation!")
print("\n")
input("Press RETURN to exit..")