# Thomas Calhoun
# homework #4
# tjcalhoun@alaska.edu & jdcastro@alaska.edu 04 Feb 2016 to 10 Feb 2016
# Python 3.5.1

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
import sys

print('             The Adventures of Grog\n'
      "                ______.--------.\n"
      "               /'                \\ \n"
      "              /'\                 \\ \n"
      "          ..-'\()'\    .'''.    ./' \n"
      "         |                .'    / \n"
      "          \..}                  '\. \n"
      "           /     {      /'    '\   \\ \n"
      "          {------'    .'        '.  '| \n"
      "           \        . |           \   | \n"
      "            '\_____/  |            |   | \n"
      "             /       |             |    | \n"
      "           .'       |              |     | \n"
      "           |       |              |       | \n"
      "           |      |              |       | \n"
      "           |                    |         \\ \n\n"
      '                  Scene One\n\n\n')
print('Grog is a caveman, a bored caveman.\nGrog needs action in his life, and not from the wildlife that seems '
      'to\nalways be trying to eat him. Grog needs...        Adventure!\n\n\n')
print('You are Grog.\n\n',"\nHOW TO PLAY: Type the response in full as it reads in each scene.\n\n")

start = {
'name':'start',
'desc': 'You are in a cave, dimly lit by the light from the entrance... \n'
        'You grunt to yourself; "Today is the day!"\n'
        '"The day to leave the cave!"',
'actions': {'leave cave': 'out_cave', 'quit':'earlyOut'},
'exit':False
}

out_cave = {
'name':'out_cave'  ,
'desc' : 'Outside, you can see across the landscape... \n'
         'The mountains, looking majestic yet untamed. \n'
         'The forest, who knows what secrets are hidden within the blind of green. \n'
         'And the desert, distorted by heat on its surface, looks most dangerous.',
'actions': {'mountains': 'mountains_1', 'forest':'forest_1', 'desert':'desert_1', 'go back':'start', 'quit':'earlyOut'},
'exit':False
}

mountains_1 = {
'name':'mountains_1',
'desc':'The base of the mountain, appears to be covered by small trees and brush. \n'
       'The wildlife is active, mostly birds and a herd of caribou in the distance. \n'
       'Although, as you proceed, you did notice what appears to be claw marks on one of trees...',
'actions': { 'go back home':'out_cave', 'proceed':'mountains_2'},
'exit':False
}

mountains_2 = {
'name':'mountains_2',
'desc':'You can see for miles!\n\nBut wait... You can hear a growl from behind...\nYou turn around...\n\n'
       'A large grizzly bear is in full charge! You try to run, there is no good cover or obstacles nearby!\n'
       '\nThe bear has caught you, and ends your adventure.\n',
'actions': {},
'exit':True
}

desert_1 = {
'name':'desert_1',
'desc':'A barren wasteland it seems, dry and hot. You also realize that some water sounds really good right now, \n'
       'as you have none.',
'actions': { 'go back home':'out_cave', 'proceed':'desert_2'},
'exit':False
}

desert_2 = {
'name':'desert_2',
'desc':'Thirst has become your enemy... You have lost all sense of direction and have now collapsed in the sand...\n'
       'Unfortunately, your adventure ends here.',
'actions': {},
'exit':True
}

forest_1 = {
'name':'forest_1',
'desc':'Within the shaded scenery inside the forest, it is cool and comforting. There is a calm creek nearby, which\n'
       'is a perfect place to rest and drink some water.',
'actions': { 'continue on':'trap', 'go back home':'out_cave'},
'exit':False
}

forest_2 = {
'name':'forest_2',
'desc':'After that scary encounter, you come across an abandoned hunting camp... It was a good thing you didn\'t wait\n'
       'for help! As you venture on, you notice what appears to be a trail along another stream...',
'actions': { 'follow trail':'pigmy_village', 'cross stream':'forest_3'},
'exit':False
}

forest_3 = {
'name':'forest_3',
'desc':'A little wet from crossing the stream, you can hear some commotion downstream... Hiding behind a bush, you \n'
       'watch closely at a small village in the distance, the locals are harassing another lone adventurer...\n'
       'After watching the unsuspecting adventurer get captured, you decide it is time to move on!',
'actions': { 'continue on':'forest_4'},
'exit':False
}

forest_4 = {
'name':'forest_4',
'desc':'Just as you are feeling exhausted from this adventure... you stumble into some bushes that reveal a clearing \n'
       'behind them... In this beautiful place you find a short cliff with a small cave opening.\n'
       '\nCould this be a new home? \n'
       'Home... You have conflicting thoughts of home, and whether or not to go back to the cave you are used to.',
'actions': { 'go back home':'out_cave', 'this is home':'finalOut'},
'exit':False
}

trap = {
'name':'trap',
'desc':'A wonderful scene this place is! The birds are singing and... *crack* ... **SWOOSH** ... \n'
       '\nYou find yourself stranded upside-down in a tree! Hanging from a vine!\n'
       'Luckily, you are not very far from the ground...',
'actions': { 'chew the vine':'forest_2', 'grunt for help':'trap_fail'},
'exit':False
}

trap_fail = {
'name':'trap_fail',
'desc':'No one responds to your plea... After some time you become light headed and pass out.\n'
       'The adventure ends here.',
'actions': {},
'exit':True
}

pigmy_village = {
'name':'pigmy_village',
'desc':'There is an active village! You are curious as you press on, but it appears these people are not fond \n'
       'of visitors... They are dressed in straw and cloth and have paint on their skin. The aggressively run \n'
       'towards you with spears, naturally you try to run... But these experienced hunters or possibly warriors\n'
       'have caught you, ending the adventure.',
'actions': {},
'exit':True
}

earlyOut = {
'name':'earlyOut',
'desc':'You have quit the Adventure. Goodbye!',
'actions': {},
'exit':True
}

finalOut = {
'name':'finalOut',
'desc':'You have completed the Adventure. Who knows what the future holds, but at this point, the moral of the story\n'
       'is to never be afraid of leaving your cave... Adventure is out there!!',
'actions': {},
'exit':True
}

map = dict ( (item['name'],item) for item in (start, out_cave, mountains_1, mountains_2, desert_1, desert_2, forest_1,
                                              forest_2, forest_3, forest_4, trap, trap_fail, pigmy_village, earlyOut,
                                              finalOut))

def game_loop(room, map):

    sys.stdout.writelines(room['desc'])

    if room['exit']:
        sys.stdout.writelines('\nThanks for playing!')
        return

    next = None

    while not next:
        sys.stdout.writelines ("\nYou can...")
        for item in room['actions'].keys():
            sys.stdout.writelines("\n\t" + item)

        sys.stdout.writelines("\n>")
        user_input = sys.stdin.readline()
        user_input = user_input.strip().lower()
        if user_input in room['actions']:
            next = room['actions'][user_input]
        else:
            sys.stdout.writelines("'%s' is not a supported option. Please try again\h" % user_input)
    game_loop(map[next], map)

game_loop (start, map)