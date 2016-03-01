#Shared with our CITS205 peeps.

from collections import Counter
import time

#The following is the start of ALOT of dramatic flair...
print("Please increase the length of your prompt window for full awesomeness...".center(80))
time.sleep(1.00)
print()
print("WELCOME TO THE BEST QUIZ THAT WE ALL KNOW AND LOVE".center(80))
time.sleep(3.00)
print()
print("ARE YOU READY".center(80))
time.sleep(2.00)
print()


#we were suprised to see that ASCII art works just fine in python.
vaultBoy = """
                                          ,▄▄▄
                                       ▄▓█▀▀▀▀▀█▄
               ▄▄▓█`       ,▄▄▓▓▄▄▄▄▄@██▀!√√√√√└▀█▄
            .▓█▀██       #█▀▀└:.!╙▀▀██▀:√√√√√√√√√!▀▀█▓▓▄▄
           ╓█▀..▀█▓▄▄▄▄▓▀▀:√√√√√√√√√√√√√√√√√√√√√√√√√░░▀▀██▄
           ██.√√√!▀▀▀▀▀:√√√√√√√√√√√√√√√√√√√√√√√√√√√√╠░░░░▀█▄
           █▌√√√√√√√√√√√√√▄▄▄▄▄.√√√√√√√╓▄▄▄.√√√√√√√√╠░░░░░╙█▄
           ██.√√√√√√√√√▄#█▀╙`╙▀█▓▄▄▄@▓██████▄.√√√√√╠░░░░░░░╙█▓▄
         ┌████:√√√√√(▄█▀╙       └▀▀▀▀└   └▀▀██,√√╓╢░░░░░░░░░░▀██▄
         ██:√╙▀▓▄▄▓▓▀▀                      └██▄░░░░░░░░░░░░░░░██▄
         █▌√√╓██▀  ▄▄@╕                       ▀▀█▓▀▀▀▀▀▀███▄░░░░██▄
         ██▄▓█▀  ╙▀▀▀▀▀                 ,▄               ▀███░░░░██▄
          ███`                         ▓███,     .        ███░░░░║██
         ▓█▀     ,▄                     └▀██▄            ▄██▀░░░░░██`
        ██▀     ███¼        ,              ▀▀        ╓@██▀▀░░░░░░░██
       ██▀     ▐███       ╓█▀        ▄▄,          .  ▄╙▀█░░░░░░░░╟██
      ▐█▌       ▀▀└     .▓█└        #███          .  ╙█▓,▀█░░░░░░██▌
      ██              ▄▓█▀          ███▌          . .▄,▀█▄╙█░░░░███
     ╟█▌            #██▀            ╙▀▀           .  ▀█▓,█▄╙█░░███
     ██─            ███                             ▓▄,▀█▄█,█░███`
     ██             ╙███                         .   ▀█▄╙█Ö█████
     ██    ,#         ╙╙                         . ╙█▄ ▀ ╙████▀
     ██  ╒███▄▄                  ▐█▄            .   ╙▀  .@███┘
     ██▌  ██▄ └╙▀▀#╦▄▄▄▄▄▄▄▄▄▄▄▄#████▄         .         ╙███
     ▐██   ▀ ▀▓▄,     `└╙└└ .      ███▌        .          ╟██
      ██▌      ╙▀█▓▄▄▄,   .,▄▄▄▓▓▀▀╙██        .          .███
      └██▄        └▀▀▀███▀▀▀▀╙"     ▀       ..          ▄███
       ╙██▄       Ñ▓▓▓▓µ                   ..    ▄▓▓▓▓███▀`
        └██▄        `└└                  ..    ▄███▀└└
          ▀██▄                          .   ▄▓██▀└
            ▀█▓▄                     ..  ▄▓██▀╙
              ╙▀█▄,                .╓▄▓██████
                 ╙██▓▄         ...   '' ▄██▀
                  ╙█████▓▓▄▄▄▄      .▄▄██▀'
                    ▀█████▄▄▄▄▄▄▄▄▓████▀
                       ╙▀▀▀██████▀▀▀╙
"""

#Disctionary to house our quiz.
answerDict = {
    "\n\nYou are approached by a frenzied vault scientist who yells \"I'm going to put my quantum harmonizer in your\n"
    "photonic resonation chamber!\" What do you say?\n"
    :{"A":" A. But doctor, wouldn't that cause a parabolic destabilization of the fission singularity?\n",
      "B":"B. \"Yeah? Up yours too, buddy!\"\n",
      "C":"C. Say nothing, but grab a nearby pipe and hit the scientist in the head to knock him out. \n    For all you"
          " knew, he was planning on blowing up the vault.\n",
      "D":"D. Say nothing, but slip away before the scientist can continue his rant.\n"},
    "\n\nWhile working as an intern in the clinic, a patient with a strange infection on his foot stumbles through"
    " the\n door. The infection is spreading at an alarming rate, but the doctor has stepped out for a while.\n "
    "What do you do?\n"
    :{"A":" A. Amputate the foot before the infection spreads.\n",
      "B":"B. Scream for help.\n",
      "C":"C. Medicate the infected area to the best of your abilities.\n",
      "D":"D. Restrain the patient, and merely observe as the infection spreads\n"},
    "\n\nYou discover a young boy lost in the lower levels of the vault. He's frightened and hungry, but also\n"
    "appears to be in possession of stolen property. What do you do?\n"
    :{"A":" A. Give the boy a hug and tell him everything will be ok.\n",
      "B":"B. Confiscate the property by force, and leave him there as punishment.\n",
      "C":"C. Pick the boy's pocket to take the stolen property for yourself, and leave the boy to his fate.\n",
      "D":"D. Lead the boy to safety, then turn him over to the Overseer.\n"},
    "\n\nCongratulations! You made one of the vault 101 baseball teams! Which position do you prefer?\n"
    :{"A":" A. Pitcher\n",
      "B":"B. Catcher\n",
      "C":"C. Designated Hitter\n",
      "D":"D. None, you wish the vault had a soccer team.\n"},
    "\n\nYour Grandmother invites you to tea, but you're surprised when she gives you a pistol and orders you to kill\n"
    "another vault resident. What do you do?\n"
    :{"A":" A. Obey your elder and kill the vault resident with the pistol.\n",
      "B":"B. Offer your most prized possession in exchange for the vault resident's life.\n",
      "C":"C. Ask for a minigun instead. After all, you don't want to miss.\n",
      "D":"D. Throw your tea in granny's face.\n"},
    "\n\nOld Mr. Abernathy has locked himself in his quarters again, and you've been ordered to get him out.\n"
    "How do you proceed?\n"
    :{"A":" A. Use a bobby pin to pick the lock on the door.\n",
      "B":"B. Trade a vault hoodlum for his cherry bomb and blow open the lock.\n",
      "C":"C. Go to the armory, retrieve a laser pistol, and blow the lock off.\n",
      "D":"D. Just walk away and let the old coot rot.\n"},
    "\n\nOh no! You've been exposed to radiation, and a mutated hand has grown out of your stomach! Whats the best \n"
    "course of treatment?\n"
    :{"A":" A. Bullet to the brain.\n",
      "B":"B. Large Doses of anti-mutagen agent.\n",
      "C":"C. Prayer, Maybe God will spare you in exchange for a life of pious devotion?\n",
      "D":"D. Removal of the mutated tissue with a precision laser.\n"},
    "\n\nA fellow Vault 101 resident is in possession of a Grognak the Barbarian comic book, issue number 1.\n"
    "You want it. What's the best way to obtain it?\n"
    :{"A":" A. Trade the comic book for one of your own valuable possessions.\n",
      "B":"B. Steal the comic book at gunpoint.\n",
      "C":"C. Sneak into the resident's quarters, and steal the comic book from his desk\n",
      "D":"D. Slip some knock out drops into the resident's Nuka Cola, and take the comic book when he's"
          " unconscious.\n"},
    "\n\nYou decide it would be fun to play a prank on your father. You enter his private restroom\n"
    "when no one is looking, and...\n"
    :{"A":" A. Loosen some bolts on the sink. When the sink is turned on, the room will flood.\n",
      "B":"B. Put a firecracker in the toilet. That's sure to cause some chaos.\n",
      "C":"C. Break into the locked medicine cabinet and replace his high blood pressure medication with sugar pills.\n",
      "D":"D. Manipulate the power wattage on his razor, so he'll get an electric shock next time he uses it.\n"},
}
#the last question needed to be forced outside the loop, otherwise the 'for' loop randomizes all keys.
lastqDict = {
    "Who is indisputably the most important person in UAF OIT: He who shelters us from the harshness of the atomic\n "
    "wasteland, and to whom we owe everything we have including our lives?\n"
    :{"A":" A.	Mrs Okinczyc.\n",
      "B":"B.	Mrs Okinczyc.\n",
      "C":"C.	Mrs Okinczyc.\n",
      "D":"D.	Mrs Okinczyc.\n"},
}
ansRecord = [] #empty list to store our user's answers
sortedGrade = None #blank object so we can call the score later for review outside the function.

def opening_statement(): # our inital loop to tease the test taker...
    print(vaultBoy.center(80))
    time.sleep(3.00)
    print("Welcome to the Generalized Occupational Aptitude Test, also known as the G.O.A.T.!".center(80)+"\n\n")
    welcomeInp = input("Are you Ready to begin?! [Y / N]:   ").upper()
    if welcomeInp == "N":
        welcomeVerify = input("Are you the Vault Overseer? [Y / N]:  ").upper()
        if welcomeVerify == "Y":
            print("I'm sorry, but that response is inaccurate. You will receive a 10% penalty on your total Aptitude"
                  "score.\n\n")
        else:
            print("Without taking the G.O.A.T, you will automatically be selected for PLUMBING ASSISTANT, \n"
                  "and placed on a continuous Jury Duty rotation until the G.O.A.T. is completed.\n\n")
    print("\n")

def goat_loop(): # the engine of our test, the loop to call our dictionary out in a user friendly output.
    print("\n"+"Stand by".center(80)+"\n")
    time.sleep(2.00)
    print("\n"+"BEGIN!".center(80)+"\n")
    time.sleep(2.00)
    tick = 0  #tick is needed to iterate for the number of questions, or else you'll be taking this test forever....
    while tick < 9:
        for quest,choices in answerDict.items():
                print(quest)
                time.sleep(1.00)
                print(choices.get("A"),choices.get("B"),choices.get("C"),choices.get("D"))
                userInput = input("Your Answer:  ").upper()
                ansRecord.append(userInput)
                tick += 1
                if userInput in ("A","B","C","D"): # a quick error check
                    continue
                else:  # ...a merciless one at that.
                    print("\nERROR!!! You entered a selection that is not supported, "
                          "please restart the test...\n\n\n".center(80))
                    tick = 0
                    goat_loop()

def last_q_loop(): #final loop for the final question. (wanted to build up to this one haha)
    tick = 0
    while tick < 1:
        for quest,choices in lastqDict.items():
                print(quest)
                time.sleep(1.00)
                print(choices.get("A"),choices.get("B"),choices.get("C"),choices.get("D"))
                userInput = input("Your Answer:  ").upper()
                ansRecord.append(userInput)
                tick += 1
                if userInput in ("A","B","C","D"):
                    continue
                else:
                    print("\nERROR!!! You entered a selection that is not supported, "
                          "please restart the test...\n\n\n".center(80))
                    tick = 0
                    goat_loop()

def grading_protocol(): # to get the grades to sort correctly, we imported the counter module to assign a score
    global sortedGrade #made this global to be called outside of the function
    dictatedAnswers = Counter(ansRecord) #our list of answers will need to be have the values counted.
    sortedGrade = dictatedAnswers.most_common() #using the power of the imported module to sort for the highest value.
    for grade in sortedGrade[0][0]: #...so that this following conditionals will the highest value.
        if grade is "A":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nWASTE MANAGEMENT "
                  "SPECIALIST\n\nIt says here you're perfectly suited for a career as a Waste Management Specialist. "
                  "A specialist, mind you, not just a dabbler. Congratulations!\n".center(80))
        if grade is "B":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nLAUNDRY CANNON OPERATOR\n\n"
                  "Well according to this, you're in line to be trained as a laundry cannon operator. First time for "
                  "everything indeed.\n".center(80))
        if grade is "C":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nJUKEBOX TECHNICIAN\n\n"
                  "Thank goodness. We're finally getting a new Jukebox Technician. That thing hasn't worked right "
                  "since old Joe Palmer passed.\n".center(80))
        if grade is "D":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nLITTLE LEAGUE COACH\n\n"
                  "I always thought you'd have a career in professional sports. You're the new vault Little League "
                  "coach! Congratulations.\n".center(80))

def view_score(): #threw this in to serve as a visualisation for the user on how the score was calculated.
    global sortedGrade
    asktoView = input("Would you like to review your score from the G.O.A.T.?".center(80)+"\n[Y / N]:   ").upper()
    if asktoView == "Y":
        print("\nBelow is how your new job was determined, by sorted list values:\n")
        print(sortedGrade)
        print("\n")

# and at last, the order of operations.
opening_statement()
goat_loop()
last_q_loop()
grading_protocol()
print("You're nuclear apocalypse begins now...".center(80)) #more dramatic flair...
print('''
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\\\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\\\ \     )
                        (/ / //  /|//||||\\\\  \ \  \ _)
''')
print("\n")
view_score()
input("Press <ENTER> to close...".center(80)) #to give you a moment to gaze in awe before the script closes. :)