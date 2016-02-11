# Thomas Calhoun
# homework #3
# tjcalhoun@alaska.edu 28 Jan 2016
# Python 3.5.1
dblLineBrk = "\n"*2 # Double Line Return
lineSep = ">-<"*25 # To add some decorative flair
newTask = (dblLineBrk+"\n"+lineSep+dblLineBrk) # Combination of the aforementioned.
pauseStmt = "Press enter to continue on!\n"


#TODO : Reference pg. 67 in textbook.
# 1) Create a list called "years_list", from 1 to 5 years old.
years_list = [1991,1992,1993,1994,1995]

# 2) In which year in "years_list", was the third b-day? (note, 1st yr is "0")
print("The year of my third birthday:\n",years_list[2],newTask)


# 3) What year in "years_list", was I oldest?
print("The year I was 5 was...:\n",years_list[4],newTask)


# 4) Make a list called "things" with 'mozzarella','cinderella','salmonella'
things = ["mozzarella","cinderella","salmonella"]
print("Now, we have a list of things:\n",things,newTask)


# 5) Capitalize the element in "things" that refers to a person, then print.
t1, t2, t3 = things #unpacked the list into string variables, more fun to manipulate it this way!!
t2 = t2.title() #reassigned the variable to keep the change permanent
things = [t1,t2,t3]
print("Notice that the individual in our list of things has been capitalized!\n",things,newTask)


# 6) Make the cheezy element of "things" all upper-case.
t1 = t1.upper()
things = [t1,t2,t3]
print("Now our cheesy thing gets the attention it deserves!:\n",things,newTask)


# 7) Delete the disease element of "things", then print.
del things[-1]
print("Finally, a list we can enjoy!(Removing the latter is like\n",
    "saving you from the effect of eating at Taco Bell!):\n",things,newTask)


# 8) Create a list called "surprise" with elements Groucho, Chico, and Harpo... But I added my own spin.
history101 = ["Nina","Pinta","Santa Maria"]
print("At last, we work with a new list:\n",history101,newTask)


# 9) Lowercase the last element of "surprise", reverse order and print.
h1, h2, h3 = history101
h3 = h3.lower()
history101 = [h1,h2,h3]
history101.sort(reverse=True)
print("But, as duty calls, the most fun ship has been subdued to all lowercase,\n"
      "and moved to the front of the lineup:",history101,newTask)


#10) Make an English-to-French dictionary called "e2f" and Print it. Starter words dog:chien, cat:chat, walrus:morse.
e2f = {
    "dog":"chien",
    "cat":"chat",
    "walrus":"morse",}
print("And now, from cerebral cortex of my text book,\n"
      "a short English to French Dictionary. (and I don't know French):\n",e2f,newTask)


#11) Using the "e2f" dict, print the french word for Walrus.
print("Behold, the French word for Walrus:\n",e2f.get("walrus"))


#12) Make a French-to-English dictionary called "f2e" from "e2f". Use ITEMS method.
e2ft1, e2ft2, e2ft3 = list(e2f.items())
f2et1 = e2ft1[::-1]
f2et2 = e2ft2[::-1]
f2et3 = e2ft3[::-1]
f2eList = [f2et1,f2et2,f2et3]
f2e = dict(f2eList)

#13) Using "f2e", print the English equiv of the french word chien.
frQuestion = input("Do you speak French? (Y/N):  ")
if frQuestion == "Y":
    print("Le mot anglais pour chien est:\n",f2e.get("chien"),newTask)
elif frQuestion == "y":
    print("Le mot anglais pour chien est:\n",f2e.get("chien"),newTask)
else:
    print('Ever wondered what the French word "chien" means? See below!:\n',f2e.get("chien"),newTask)

#14) Make and print a set of English words from the keys in "e2f"
englishOnly = set(e2f)
print("As a matter of fact, this is all I have from the French to English dictionary:\n",englishOnly,"\nI know,"
    "I best get busy to catch up to the other published dictionaries!",newTask)

#15) Make a multi-level dictionary called "life", use these strings for the topmost keys:
#>>> 'animals', 'plants', and 'other'. Make 'animals' key refer to other dict on animals.
#>>> Assign dictionaries to those dict keys with names.

#I have to warn you, I went overboard with idea of "I don't wanna use the book examples because everyone else might be
#  doing the same (And my creativity for random keys and values was nonexistent at the time), so why not have
#  Jeanette enter input the dictionary as a practical coding exercise?"
#So here it is, almost a week or research and coming dangerously close to gouging my eyes out over nonfunctional
# conditional statements, I present a short dictionary cataloging program in my assignment!
#........................(Maybe I can improve on this later in the semester)..........................................

pets = {}
petBreed = None
petName = None
wildAnim = {}
wildWhere = None
wildName = None
favPlants = {}
plantType = None
plantName = None
favCars = {}
carBrand = None
carModel = None
input("\n\nLOOPING QUESTIONS, if you do not have an answer, just fill with 'none' or 'n/a'.\n\n"
      "You will get a chance to go back and add something or correct a key \n(no delete function, yet...)"
      "\n\nPress enter to continue...\n\n")
print("Please press 'Enter' or 'Return' on your keyboard to begin the following categories:"
      "\nA:Pet entry...\nB:Wild Animal entry...\nC:Plants entry\nD:Cars entry\n")
finText = "\n\nFinished (Y/N)?\n"
notFinResp = "\n\nNext Entry...\n"

#last minute swap of variable placement (on a few of the functions) to keep the dict key descriptive.
def setPetDict():
    while (True):
        print("For the critter(s) we like to keep close by!\n\n")
        petBreed = input("Pet Breed?:\n")
        petName = input("Pet Name?:\n")
        pets[petName] = petBreed
        finQuest = input(finText)
        if finQuest in ("y","Y"):
            break
        else:
            print(notFinResp)
    return True

def setWildDict():
    while (True):
        print("Tell us what you favorite 'wild things' are!\n\n")
        wildWhere = input("Where does this creature lurk?:\n")
        wildName = input("Animal Name?:\n")
        wildAnim[wildName] = wildWhere
        finQuest = input(finText)
        if finQuest in ("y","Y"):
            break
        else:
            print(notFinResp)
    return True

def setPlantDict():
    while (True):
        print("Reach deep for that inner botanical passion!\n\n")
        plantType = input("Favorite plant type (Tree, Vine, Cactus, etc...)?:\n")
        plantName = input("Plant Name?:\n")
        favPlants[plantName] = plantType
        finQuest = input(finText)
        if finQuest in ("y","Y"):
            break
        else:
            print(notFinResp)
    return True

def setCarDict():
    while (True):
        print("Vrooooooom!\n\n")
        carBrand = input("Brand of Favorite Vehicle?:\n")
        carModel = input("Year (optional) & Model Name?:\n")
        favCars[carModel] = carBrand
        finQuest = input(finText)
        if finQuest in ("y","Y"):
            break
        else:
            print(notFinResp)
    return True

def printAllDict():
    while (True):
        printResult = input("\nWould you like to review your entries? (Y/N):\n")
        if printResult in ("n","N"):
            break
        elif printResult in ("y","Y"):
            spacer = ("\n"+"~*"*15+"\n")
            print("\nItems below listed in a 'KEY : VALUE' Pair...",spacer,"PETS:\n",pets,spacer,"WILD ANIMALS:"
                                               "\n",wildAnim,spacer,"PLANTS:\n",favPlants,spacer,"VEHICLES:\n",favCars)

def dictEntryProcess():
    print("\n\nLets set some favorite pets!\n\n")
    setPetDict()
    print("\n\nLets set some favorite wild animals!\n\n")
    setWildDict()
    print("\n\nLets set some favorite plants!\n\n")
    setPlantDict()
    print("\n\nLets set some favorite vehicles!\n\n")
    setCarDict()
    printAllDict()

def lastChance():
    questionOfTheCentury = input("\n\nDo you want to make any modifications to those dictionaries? (Y/N):\n")
    while (True):
        if questionOfTheCentury in ("n","N"):
            break
        elif questionOfTheCentury in ("y","Y"):
            chgDictSelect = input("\nPlease select Dictionary you would like to change:\n[A] Pets\n[B] Wild Critters\n"
                                  "[C] Plants\n[D] Automobiles.\n[X] To Cancel\n>>> SELECTION:   \n\n")
            if chgDictSelect in ("a","A"):
                setPetDict()
            elif chgDictSelect in ("b","B"):
                setWildDict()
            elif chgDictSelect in ("c","C"):
                setPlantDict()
            elif chgDictSelect in ("d","D"):
                setCarDict()
            elif chgDictSelect in ("x","X"):
                break

dictEntryProcess()
lastChance()

print(newTask)

#And the data structure take form...
movingLife = {"Domestic" : pets,"Wild" : wildAnim,}
stationaryLife = {"Plants" : favPlants,}
transportLife = {"Vehicles" : favCars,}
life = {"Moving Life" : movingLife,"Stationary Life" : stationaryLife, "Transportation" : transportLife,}

#16) Print the top-level keys of "life".
print("At this stage, your fingers might be tired... So relax and checkout the combined\n"
      " form of your entries, in a dictionary we call 'Life':\n",life.keys(),newTask)

#17) Print the keys for "life" [animals]
print("\nA look at the keys for 'Moving Life':\n\n",life["Moving Life"].keys(),newTask)

#18) Print the values for "life" [animals][cats].
print("\nLets a go bit deeper for 'Domestic' critters keys:\n\n",life["Moving Life"]["Domestic"].values(),newTask)

input("\n\nAnd there we have it. Week 3 Assignment plus some more. See you in class!\n"
      "   Press enter to finish the process...")