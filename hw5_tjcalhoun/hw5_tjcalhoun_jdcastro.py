# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 04 Feb 2016 to 10 Feb 2016
# Python 3.5.1

import sys
#The GOAT!

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
print("Welcome to the Generalized Occupational Aptitude Test,\nalso known as the G.O.A.T.!".center(80))
input("\n\nPress the <ENTER> Key to continue...".center(80))



# --- Stuff that I'm gonna hack up, from an abandoned game idea ---


q1 = {
'name':'Q1',
'desc': '...',
'actions': {'Answer1': 1, 'Answer2': 2,'Answer3': 3,'Answer4': 4,},
'exit':False
}

#map = dict((item['name'],item) for item in (q1,))

#def game_loop(room, map):  #Killed the following code, to use as inspiration for our new quiz engine.
#    sys.stdout.writelines(room['desc'])
#
#    if room['exit']:
#        sys.stdout.writelines('\nThank you for time, and good luck in your Vault career!')
#        return
#    next = None
#    while not next:
#        sys.stdout.writelines ("\nChoose your response...")
#        for item in room['actions'].keys():
#            sys.stdout.writelines("\n\t" + item)
#        sys.stdout.writelines("\n>")
#        user_input = sys.stdin.readline()
#        user_input = user_input.strip().lower()
#        if user_input in room['actions']:
#            next = room['actions'][user_input]
#        else:
#            sys.stdout.writelines("'%s' is not a supported option. Please try again\h" % user_input)
#    game_loop(map[next], map)

#game_loop (q1, map)