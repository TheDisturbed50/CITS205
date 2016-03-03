# Thomas Calhoun & Jose Castro
# homework #7
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 25 Feb 2016 to 03 Mar 2016
# Python 3.5.1

from newmods import menugen, zoo, goat, guess, age #imported Modules names are small enough, no alias needed.
from collections import OrderedDict, defaultdict
import pprint, time, random

spacer = ("+="*39)+"\n"  # a fancy effect for the main menu

def assignment_stuffs():  # for the defaultdict part of the assignment...
    print("A heads up, if you skipped option \"2\", you will be sadly disappointed by this section.\n"
          "But no worries, following this section will be another opportunity!\n")
    userMenu = OrderedDict(menugen.menu)  # taking the work from a module option to iterate
    print("This section is iterating the modifiable diction you constructed in menu option\n"
          "number \"2\", called {}. You may notice the sort by keys (item name).".format(menugen.mTitle))
    print("\n", userMenu, "\n")
    input("Press the ENTER key to continue...".center(80))

    dict_of_lists = defaultdict(list)  # initiating the defaultdict

    print("Behold, the Dict of Lists...\n",dict_of_lists, "\n (Yes, its empty... I know.)")
    dict_of_lists["a"]  # assignment of the key
    print("\nAnd now, with a defaultdict assignment...\n",dict_of_lists,"\n")
    print("Now, for this last part of the assignment, I will ask for\n some participation in the audience (you).\n")

    while True:  # to make it a little more lively, a process to allow the user to enter their own values.
        print("\n\n")
        askUserAppend = input("Please type a value to insert for key \"a\" in the defaultdict\n"
                              "(Spaces not tolerated within entry)... VALUE: ")
        print("\n")
        dict_of_lists["a"].append(askUserAppend)
        print("This will be displayed in a KEY : VALUE pair:".center(40))
        pprint.pprint(dict_of_lists,indent=4,  width=1)  # using pprint to help with presentation.
        print("\n")
        askUserCont = input("Continue adding Values? [ Y / N ]:".center(80)).lower()
        if askUserCont == "n":  # allow the user to break the process when done
            return False


def wrong_input():  # why not troll someone if they don't follow the menu? Some lessons are best taught in sarcasm!
    trollDict = {
        1:"""
         AAAARG!!!! DOES THAT LOOK LIKE IT WAS ON THE MENU?!?!
                                                     ___,------,
             _,--.---.                         __,--'         /
           ,' _,'_`._ \                    _,-'           ___,|
          ;--'       `^-.                ,'        __,---'   ||
        ,'               \             ,'      _,-'          ||
       /                  \         _,'     ,-'              ||
      :                    .      ,'     _,'                 |:
      |                    :     `.    ,'                    |:
      |           _,-      |       `-,'                      ::
     ,'____ ,  ,-'  `.   , |,         `.                     : \\
     ,'    `-,'       ) / \/ \          \                     : :
     |      _\   o _,-'    '-.           `.                    \ \\
      `o_,-'  `-,-' ____   ,` )-.______,'  `.                   : :
       \-\    _,---'    `-. -'.\  `.  /     `.                  \  \\
        / `--'             `.   \   \:        \                  \,.\\
       (              ____,  \  |    \\\\        \                 :\ \\\\
        )         _,-'    `   | |    | \        \                 \\\\_\\\\
       /      _,-'            | |   ,'-`._      _\                 \,'
       `-----' |`-.           ;/   (__ ,' `-. _;-'`\           _,--'
     ,'        |   `._     _,' \-._/  Y    ,-'      \      _,-'
    /        _ |      `---'    :,-|   |    `     _,-'\_,--'   \\
   :          `|       \`-._   /  |   '     `.,-' `._`         \\
   |           _\_    _,\/ _,-'|                     `-._       \\
   :   ,-         `.-'_,--'    \                         `       \\
   | ,'           ,--'      _,--\           _,                    :
    )         .    \___,---'   ) `-.____,--'                      |
   _\    .     `    ||        :            \                      ;
 ,'  \    `.    )--' ;        |             `-.                  /
|     \     ;--^._,-'         |                `-._            _/_\\
\    ,'`---'                  |                    `--._____,-'_'  \\
 \_,'                         `._                          _,-'     `
                            ,-'  `---.___           __,---'
                          ,'             `---------'
                        ,'
                      NO!     ...IT SURE WASN'T!!!!
        """,
        2:"""
                   D'OH!
                                    __
                       _ ,___,-'",-=-.
           __,-- _ _,-'_)_  (""`'-._\ `.
        _,'  __ |,' ,-' __)  ,-     /. |
      ,'_,--'   |     -'  _)/         `\\
    ,','      ,'       ,-'_,`           :
    ,'     ,-'       ,(,-(              :
         ,'       ,-' ,    _            ;
        /        ,-._/`---'            /
       /        (____)(----. )       ,'
      /         (      `.__,     /\ /,
     :           ;-.___         /__\/|
     |         ,'      `--.      -,\ |
     :        /            \    .__/
      \      (__            \    |_
       \       ,`-, *       /   _|,\\
        \    ,'   `-.     ,'_,-'    \\
       (_\,-'    ,'\\")--,'-'       __\\
        \       /  // ,'|      ,--'  `-.
         `-.    `-/ \\'  |   _,'         `.
            `-._ /      `--'/             \\
               ,'           |              \\
              /             |               \\
           ,-'              |               /
          /                 |             -'

    YOUR IMAGINATION WENT WILD ON THAT SELECTION...

        """,
        3:"""
        SEE?!?!      THIS. THIS IS WHAT HAPPENS WHEN YOU TRY TO BREAK SOMEONE'S CODE...
                           .,,-=:==;.
                        .-==--,,...,-
                     .,==-,.    ,..,.-.
                   .-=-,.   .,   ,. .,,-
                  -=-.   ,   .,.  ,. .,.,,
                  ;-. ,. .,   .,   .,  .,.-.
                  ,,,..,  .,   .,   .,  .,..,
                   =., ..  ,.   .,   .,   ,, ,,
                   : ,  ,   ,.   .,   ..   .. .-.
                   = ,. ..  .,    ....,----=====:-,
                   -..,  ,   ., .,-===::;/+%%====:==
                   ., ,  ., .,-===;+$HH#####X:,,,===
                    = ,.  .-==:/$H###########$=====.
                    : ...===;$H###############X/=,
                    =..-==/X############X$@##H@X.
                    ,-=-;$######$XXXXXXX$XXXXXHH:
                    .%-:-+#####@@#H+:=-==/=,..;,:
                     =-:-:X#$$@X;, -,    :--=-  =
                     .=-:;/X%H$H/.     .:X@##H%$.
                       .-:,%$#H$#X+;::+%H#HHX+;/-
                         - :$X####XXX$/;:==-----:.
                          -$$X#####H;=-----------:.
                          -$$XH###X=-----==-:--:=-:
                           -/$@##H:--==-.==-;:;:=-,
                            -@###%--/=;X$#@:==.
                            -H###/-+###@@@H-:
                          :-:H###%-$H#HH@H+::-
                         , .-/H##X:=///;:---:;.
               .........,.     ,:+$;=----=:%;.,:-.......,.
           ...           ,         ,-:/+%XH#+.-...      :X+:--,.
         .,               ..           --$##X=-  ,     /H#####HHX$/:=-,..
        =X$/=.             -          .  ,$##%-. ,    ;H###############@HX$$/;=-,,--=:;/%$$/-
      ,$H####X;,           ,,..       ,   .%#; .-,   ,X#####################################X=
    .;H########H;.         ,   ....   .    .;,  ..   /##############################@X$$$%=-,
   ,%############$-        .        .,           .  .$#############################H$H#X$X+
  -X##############X=      ,                       , ,$##########################X@$$X##X$#X,
 ,X################$,    ,                        ...$#####################@@###HHX$X#H$@#%
 %################%==  ,.                          .-$#######@##@@HX$++/;::=:$#####X$$$XX;.
,X###############/=,:-=                              .;::,.....               ,=;;:-.
,X##############X, . .                                 ,.
 ;@##############%.  ,                                  .,
  /###############$;.                                     -
   ,%##############X: .                                   .,
     -%H############@%,.                                   -
       ,;H###########@;                                     =
          :H#########@:                                     :
         .,$##########+.                                    -
        .$H$#########+,                     .......,....... -
         +#X$#######+          ...,,,,,,,,,................=.
         .=H#####@$=.   .,,,,,,............................=
            =+$//,..,,,,...................................-
                ,:;.......................................=
                 ,,=.....................................,=
                    =.....................................-
                    .=....................................,.
                     ,,....................................-
                     -.....................................-
                     =.................,---................,.
                     =.................-=-..................-
                     =................,. =..................=
                    .-................,  =..................,.
                    ,,................-  ,-..................-
                    -.................-   =..................-
                    =.................-   =..................,,
                    =.................=   .-..................:
                    -.................-    =..................=
                   .,.................,    =..................,,
                   ,.................,.    .,..................=
                   -.................-      =..................-
                   -.................=      -..................,
                   =.................=      .,..................,
                   -.................-       -..................,
                  ,,.................,       -..................-
                  -,................,.       ,,................,=,
                  :---,,,........,,-:.        :----,-,,,,-----,,.-
                 .-....,,,,,,,,,,,..-.        =..................-
                 .,.................=         =.................,;.
                 =+;:==---------==://          ;:=---------==:;++/+;.
               .///////+//+//+//////+-         :////////////////////+:
              .+////////////+///////+-         .=++/+++////////////////
              :///////+/////////:;=,              .,=-=/////+/////////+=
              +////////////++;-.                       .-;/++///////////
              ////////++;=,.                                .-=;/++/////
              .;;:=-,.                                             .,,.

                   BLEEEEERRRRRRRP!!!!
        """,
    }
    keyPicker = random.randint(1,3)  # to randomly pick our troll option
    print(trollDict[keyPicker])
    time.sleep(1.30)


# opening sequence.
print("From the people who brought you".center(80))
print()
time.sleep(2.00)
print("The Goat".center(80))
time.sleep(2.00)
print()
print("And".center(80))
time.sleep(1.00)
print()
print("Guess the number".center(80))
time.sleep(2.00)
print()
print("And i Guess this Guy...........".center(80))
print()
time.sleep(2.00)
print("""


           .'''*(7????(C?!!,''.                                           
           '!(7(!,,!?,,,,!!,,!!C!!,       
        '!(?,,,?,,,,,,,,,,,,,,,(,,!7!'      
       !?((,,,,,,,,,,,,,,,,,,,,,,,,*C??        
     ?=*,,,,,?!!,,,,,,,,,,,,,,,,,,,,,,,=*                                   
   .?((,,,,*?((=C=!,,,,,,,,,,,,,,,,,**,((*    
 .*=!,,,,,?!.    *(*,,,,,,,,,,,,*(=77(!,,?*   
 ==?,,,,,,(   ?   .=,,,,,,,,,,,*(*'''!?,,,C.    
 ===,,,,,,(  .,.. .7,,,,,,!?,,,=   ', '(,,??   
   '(*,,,,(C=?!!?7C*,,,,,,*7,,*=,,,,,  =,,,(=,    
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
""")
time.sleep(2.00)
print()
print("Comes the most anticipated project of the semester".center(80))
print()
time.sleep(2.00)
print("That brings all the projects under one Menu".center(80))
print()
time.sleep(2.00)
print("The most epic 10-point assignment of the season....".center(80))
print()
time.sleep(2.00)
print("Presenting".center(80))
print()
print("The.........")
time.sleep(3.00)
print(""" 
                              . .  ,  ,
                              |` \/ \/ \,', 
                              ;          ` \/\,. 
                             :               ` \,/
                             |                  / 
                             ;                 : 
                            :                  ; 
                            |      ,---.      / 
                           :     ,'     `,-._ \ 
                           ;    (   o    \   `' 
                         _:      .      ,'  o ; 
                        /,.`      `.__,'`-.__, 
                        \_  _               \ 
                       ,'  / `,          `.,'      SUCKER!!!!!!
                 ___,'`-._ \_/ `,._        ; 
              __;_,'      `-.`-'./ `--.____) 
           ,-'           _,--\^-' 
         ,:_____      ,-'     \ 
        (,'     `--.  \;-._    ; 
        :    Y      `-/    `,  : 
        :    :       :     /_;' 
        :    :       |    : 
         \    \      :    : 
          `-._ `-.__, \    `. 
             \   \  `. \     `. 
           ,-;    \---)_\ ,','/ 
           \_ `---'--'" ,'^-;' 
           (_`     ---'" ,-') 
           / `--.__,. ,-'    \ 
           )-.__,-- ||___,--' `-. 
          /._______,|__________,'\ 
          `--.____,'|_________,-' 
 : :_,,--~"... ... ... ... ...\:::::::::::::::::::::::\

""")
time.sleep(2.00)
print("JUST KIDDING!!!!".center(80))
time.sleep(2.0)
print()
def home_menu():
    """
    Main Menu of the program.
    :return:
    """
    
    while True:
        print("<><>-<><> MAIN MENU <><>-<><>".center(80), "\n", '''
{}+=  [1] See the Zoo Hours!                                                  +=
{}+=  [2] Create a Fun Menu!                                                  +=
{}+=  [3] Test your skills with the Fallout 3 G.O.A.T.!                       +=
{}+=  [4] Play "Guess the Number"!                                            +=
{}+=  [5] See how long you have existed with the Age Calculator!              +=
{}+=  [6] Enough of this Tom-Foolery, get on with the assignment!             +=
{}+=  [Q] Quit Program                                                        +=
{}
        '''.format(spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer)) #printed independently to format easier
        userOption = input("Selection: ") #user input
        if userOption == "1":
            print("\n"*1)
            zoo.hours()
            print("\n"*5)
        elif userOption == "2":
            print("\n"*1)
            menugen.mainMenu()
            print("\n"*5)
        elif userOption == "3":
            print("\n"*1)
            goat.start_goat()
            print("\n"*5)
        elif userOption == "4":
            print("\n"*1)
            guess.call_to_start()
            print("\n"*5)
        elif userOption == "5":
            print("\n"*1)
            age.age_calc()
            print("\n"*5)
        elif userOption == "6":
            print("\n"*1)
            assignment_stuffs()
            print("\n"*5)
        elif userOption in ("q","Q"):
            return False
        else:
            wrong_input()  # well... you know what this does by now ;)

home_menu()
