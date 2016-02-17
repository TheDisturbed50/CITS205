# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 04 Feb 2016 to 10 Feb 2016
# Python 3.5.1
from collections import Counter
import time
time.sleep(1.00)
print("""
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
""".center(80))
time.sleep(1.00)

answerDict = {
    "You are approached by a frenzied vault scientist who yells \"I'm going to put my quantum harmonizer in your "
    "photonic resonation chamber!\" What do you say?\n\n"
    :{"A":"A. But doctor, wouldn't that cause a parabolic destabilization of the fission singularity?\n",
          "B":"B. \"Yeah? Up yours too, buddy!\"\n",
          "C":"C. Say nothing, but grab a nearby pipe and hit the scientist in the head to knock him out. \nFor all you"
              " knew, he was planning on blowing up the vault.\n",
          "D":"D. Say nothing, but slip away before the scientist can continue his rant.\n"},
    "While working as an intern in the clinic, a patient with a strange infection on his foot stumbles through the "
    "door. The infection is spreading at an alarming rate, but the doctor has stepped out for a while. What do you do?"
    :{"A":"A. Amputate the foot before the infection spreads.\n",
      "B":"B. Scream for help.\n",
      "C":"C. Medicate the infected area to the best of your abilities.\n",
      "D":"D. Restrain the patient, and merely observe as the infection spreads\n"},
    "You discover a young boy lost in the lower levels of the vault. He's frightened and hungry, but also appears to be in possession of stolen property. What do you do?"
    :{"A":"A. Give the boy a hug and tell him everything will be ok.\n",
      "B":"B. Confiscate the property by force, and leave him there as punishment.\n",
      "C":"C. Pick the boy's pocket to take the stolen property for yourself, and leave the boy to his fate.\n",
      "D":"D. Lead the boy to safety, then turn him over to the Overseer."},
    "Congratulations! You made one of the vault 101 baseball teams! Which position do you prefer?"
    :{"A":"A. Pitcher\n",
      "B":"B. Catcher\n",
      "C":"C. Designated Hitter\n",
      "D":"D. None, you wish the vault had a soccer team.\n"},
    "Your Grandmother invites you to tea, but you're surprised when she gives you a pistol and orders you to kill another vault resident. What do you do?"
    :{"A":"A. Obey your elder and kill the vault resident with the pistol.\n",
      "B":"B. Offer your most prized possession in exchange for the vault resident's life.\n",
      "C":"C. Ask for a minigun instead. After all, you don't want to miss.\n",
      "D":"D. Throw your tea in granny's face.\n"},
    "Old Mr. Abernathy has locked himself in his quarters again, and you've been ordered to get him out. How do you proceed?"
    :{"A":"A. Use a bobby pin to pick the lock on the door.\n",
      "B":"B. Trade a vault hoodlum for his cherry bomb and blow open the lock.\n",
      "C":"C. Go to the armory, retrieve a laser pistol, and blow the lock off.\n",
      "D":"D. Just walk away and let the old coot rot.\n"},
    "Oh no! You've been exposed to radiation, and a mutated hand has grown out of your stomach! Whats the best course of treatment?"
    :{"A":"A. Bullet to the brain.\n",
      "B":"B. Steal the comic book at gunpoint.\n",
      "C":"C. Sneak into the resident's quarters, and steal the comic book from his desk\n",
      "D":"D. Slip some knock out drops into the resident's Nuka Cola, and take the comic book when he's unconscious.\n"},
    "A fellow Vault 101 resident is in possession of a Grognak the Barbarian comic book, issue number 1. You want it. What’s the best way to obtain it?"
    :{"A":"A. Trade the comic book for one of your own valuable possessions.\n",
      "B":"B. Large Doses of anti-mutagen agent.\n",
      "C":"C. Prayer, Maybe God will spare you in exchange for a life of pious devotion?\n",
      "D":"D. Removal of the mutated tissue with a precision laser.\n"},
    "You decide it would be fun to play a prank on your father. You enter his private restroom when no one is looking, and..."
    :{"A":"A. Loosen some bolts on the sink. When the sink is turned on, the room will flood.\n",
      "B":"B. Put a firecracker in the toilet. That's sure to cause some chaos.\n",
      "C":"C. Break into the locked medicine cabinet and replace his high blood pressure medication with sugar pills.\n",
      "D":"D. Manipulate the power wattage on his razor, so he'll get an electric shock next time he uses it.\n"},
}
lastqDict = {
        "Who is indisputably the most important person in UAF OIT: He who shelters us from the harshness of the atomic wasteland, and to whom we owe everything we have including our lives?\n"
    :{"A":"A.	The Overseer.\n",
      "B":"B.	The Overseer.\n",
      "C":"C.	The Overseer.\n",
      "D":"D.	The Overseer.\n"},
}
ansRecord = []

def opening_statement():
    print("Welcome to the Generalized Occupational Aptitude Test, also known as the G.O.A.T.!\n\n".center(80))
    welcomeInp = input("Are you Ready to begin?! [Y / N]:  ").upper()
    if welcomeInp == "N":
        welcomeVerify = input("Are you the Vault Overseer? [Y / N]:  ").upper()
        if welcomeVerify == "Y":
            print("I'm sorry, but that response is inaccurate. You will receive a 10% penalty on your total Aptitude"
                  "score.\n\n")
        else:
            print("Without taking the G.O.A.T, you will automatically be selected for PLUMBING ASSISTANT, \n"
                  "and placed on a continuous Jury Duty rotation until the G.O.A.T. is completed.\n\n")

def goat_loop():
    print("Get ready for the next question!\n\n".center(80))
    tick = 0
    while tick < 9:
        for quest,choices in answerDict.items():
                print(quest)
                time.sleep(1.00)
                print(choices.get("A"),choices.get("B"),choices.get("C"),choices.get("D"))
                userInput = input("Answer:  ").upper()
                if userInput in ("A","B","C","D"):
                    continue
                else:
                    print("\nERROR!!! You entered a selection that is not supported, please restart the test...\n\n\n")
                    goat_loop()
                ansRecord.append(userInput)
                tick += 1

def last_q_loop():
    print("Get ready for the next question!\n\n".center(80))
    tick = 0
    while tick < 1:
        for quest,choices in lastqDict.items():
                print(quest)
                print(choices.get("A"),choices.get("B"),choices.get("C"),choices.get("D"))
                userInput = input("Answer:  ").upper()
                if userInput in ("A","B","C","D"):
                    continue
                else:
                    print("\nERROR!!! You entered a selection that is not supported, please restart the test...\n\n\n")
                    last_q_loop()
                ansRecord.append(userInput)
                tick += 1
                time.sleep(1.00)

def grading_protocol():
    dictatedAnswers = Counter(ansRecord)
    sortedGrade = sorted(dictatedAnswers.items(), key=lambda x:x[1])
    sortedGrade.sort()
    for grade in sortedGrade[0][0]:
        if grade is "A":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nWASTE MANAGEMENT SPECIALIST\n\n"
                  "It says here you're perfectly suited for a career as a Waste Management Specialist. A specialist, "
                  "mind you, not just a dabbler. Congratulations!\n")
        if grade is "B":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nLAUNDRY CANNON OPERATOR\n\n"
                  "Well according to this, you're in line to be trained as a laundry cannon operator. First time for "
                  "everything indeed.\n")
        if grade is "C":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nJUKEBOX TECHNICIAN\n\n"
                  "Thank goodness. We're finally getting a new Jukebox Technician. That thing hasn't worked right "
                  "since old Joe Palmer passed.\n" )
        if grade is "D":
            print("\nCongratulations on completing the G.O.A.T! You perfect job is...\n\nLITTLE LEAGUE COACH\n\n"
                  "I always thought you'd have a career in professional sports. You're the new vault Little League "
                  "coach! Congratulations.\n")

opening_statement()
goat_loop()
last_q_loop()
grading_protocol()
input("Press <ENTER> to close...")