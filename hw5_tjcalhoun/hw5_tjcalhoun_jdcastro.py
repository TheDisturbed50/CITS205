# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 04 Feb 2016 to 10 Feb 2016
# Python 3.5.1

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
print("Welcome to the Generalized Occupational Aptitude Test, also known as the G.O.A.T.!\n\n".center(80))
#input("\n\nPress the <ENTER> Key to continue...".center(80))

q1 = "You are approached by a frenzied vault scientist who yells \"I'm going to put my quantum harmonizer in your " \
     "photonic resonation chamber!\" What do you say?\n\n"
q2 = "Question2"
q3 = "Question3"
q4 = "Question4"
q5 = "Question5"
q6 = "Question6"
q7 = "Question7"
q8 = "Question8"
q9 = "Question9"
q10 = "Question10"

answerDict = {
    q1:{"A":"But doctor, wouldn't that cause a parabolic destabilization of the fission singularity?\n",
          "B":"\"Yeah? Up yours too, buddy!\"\n",
          "C":"Say nothing, but grab a nearby pipe and hit the scientist in the head to knock him out. \nFor all you"
              " knew, he was planning on blowing up the vault.\n",
          "D":"Say nothing, but slip away before the scientist can continue his rant.\n"},
    q2:{"A":"Sample A", "B":"Sample B","C":"Sample C","D":"Sample D"},
#    q3:{},
#    q4:{},
#    q5:{},
#    q6:{},
#    q7:{},
#    q8:{},
#    q9:{},
#    q10:{},
}

ansRecord = []

def goat_loop():
    print("Get ready for the next question!\n\n".center(80))
    #questions = answerDict.keys()
    #answers = answerDict.values()
    #funTime = {questions:answers}
    tick = 0
    while tick < 2:
        for quest,choices in answerDict.items():
                print(quest)
                print(choices.get("A"),choices.get("B"),choices.get("C"),choices.get("D"))
                userInput = input("Answer:  ")
                ansRecord.append(userInput)
                tick += 1

goat_loop()
print(ansRecord)