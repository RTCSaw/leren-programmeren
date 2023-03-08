import time
import sys
from random import randint
import random
###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################
#                                                                                                         STORY
######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################






#####################################################################################################################################################################################################################################
#####################################################################################################################################################################################################################################
#                                                                                   ALLE FUNCTIONS IN GAME DIE WORDEN AANGEROEPEN IN FUNCTIONS
######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################
def delay_print(string):
    for char in string:
        sys.stdout.write(char)     
        sys.stdout.flush()
        time.sleep(0.03)
######################################################################################################################################################################################################################################                               
#print one character at a time

def delay_input(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


######################################################################################################################################################################################################################################
#  lancering wwordt hier geactiveerd of geabort
def launch ():
  while True: 
    lanceren = input("De raket is klaar om te lanceren! Als u de lancering wilt activeren kunt u dat doen doormiddell 'LAUNCH' ").lower()
    if lanceren == "launch": 
        break
    elif lanceren == "abort":
        print("De missie om de laatste mensen te redden if afgelast... iedereen zijn vrijheid zal worden ingenomen...")
        print (game_over)
        exit()
    else: 
        print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
        aftellen10()
    print(lift_off)

######################################################################################################################################################################################################################################
# hier wordt de eerste som gegevraagd
def latitude():
  noordlat = random.randint(1,9)
  eastlat = random.randint(1,15)
  time.sleep(1)
  keuze_koers = input("Om de raket op juiste koers moeten we een kant op sturen! Kies tussen'Kies tussen Links/Rechts'")
  if keuze_koers == "links":
    
    
      print("De raket is in een juiste baan op weg naar Mars, blijf deze kant op gaan!")
      time.sleep(2)
      delay_print("Een enorme windstoot heeft de raket op een andere koers gebracht! Stuur zo snel mogelijk bij na het berekenen van de nieuwe koers!")
      try:
        noordlattitude = int(input (f'Het gegeven noordelattitude is: {noordlat} + het gegeven oosten lattitude {eastlat} is gecombineeerd?'))
        if int(noordlattitude == (noordlat + eastlat)):
          delay_print("""Dat is helemaal juist! Je hebt de jusite koers berekend en we zijn weer onderweg! """)
      except:
        delay_print("dat is fout berekend, probeer het opnieuw!!") 
        noordlattitude = int(input (f'Het gegeven noordelattitude is: {noordlat} + het gegeven Oost lattitude {eastlat} is samen gecombineeerd?'))

  print()

  if keuze_koers == "rechts":
    delay_print("Door een verkeerde input door de piloot is de raket op de verkeerde koers gebracht! Stuur zo snel mogelijk bij na het berekenen van de nieuwe koers!")
    print()
    try:
        noordlattitude = int(input (f'Het gegeven noordelattitude is: {noordlat} + het gegeven oosten lattitude {eastlat} is gecombineeerd?'))
        if int(noordlattitude == (noordlat + eastlat)):
          delay_print("""Dat is helemaal juist! Je hebt gelukkig toch de koers berekend en we zijn weer onderweg! """)
    except:
      delay_print("dat is fout berekend, probeer het opnieuw!!") 
      noordlattitude = int(input (f'Het gegeven noordelattitude is: {noordlat} + het gegeven Oost lattitude {eastlat} is samen gecombineeerd?'))
#########################################################################################################################################################################################################################################
def komeetBattle():
  from random import randint
      
  rots = 20
  while rots > 0:
      playerinput = input("""vuur ZO SNEL MOGELIJK op de komeet!!
      Type vuur om de lazers te schieten!""")                    
      damage = randint(1,6)
      if playerinput == "vuur":                                   
          rots = rots - damage                                    
          print(f"de rots heeft geschat nog {rots} hp over")
                                                                
          if rots <= 0:
            print("Je hebt de komeet kapot geschoten!! we kunnen gelukkig veilig door!")
      else:
        print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
#########################################################################################################################################################################################################################################
def Alien_battle():
  alien_leven = 20
  raket_leven = 30
  delay_print("""ER IS EEN ALIEN ONS ACHTERVOLGT!! Ga de battle aan!""")
  while alien_leven > 0:
    playerinput = input("""VUUR ZO SNEL MOGELIJK op de Aliens!!!""")           
    damage = randint(1,6)               
    alien_damage = randint(1,6)
    if playerinput == "vuur":
      alien_leven = alien_leven - damage
      raket_leven = raket_leven - alien_damage
      print(f"de Aliens heeft geschat nog {alien_leven} hp over")
      time.sleep(0.7)
      print("De aliens schieten terug, ZET JE SCHRAP!!!")
      time.sleep(1)
      print(f"De raket heeft nog ongeveer {raket_leven} hp over")
      if alien_leven <= 0:
        print("Je hebt de aliens een lesje geleerd!! We kunnen gelukkig veilig door!") 
      if raket_leven <= 0:
              print("De aliens hebben de raket kapot geschoten.... We zijn allemaal dood...")
              print(game_over)
              exit()
      else:
        print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
        raket_leven = raket_leven - alien_damage
        print(f"WE HEBBEN GEMIST EN WE ZIJN GERAAKT!!! WE HEBBEN NOG {raket_leven} hp over")
#########################################################################################################################################################################################################################################
def zuurstof():
  num1zuurstof = random.randint(1,3)
  num2brandstof = random.randint(1,5)
  while True:
    try:
        zuurstof = int(input (f'Het aantal liters in zuurstof: {num1zuurstof} + het aantal liters in brandstof {num2brandstof} is samen?'))
    except ValueError:
        print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
        continue
    else:
        break
  if int(zuurstof == (num1zuurstof + num2brandstof)):
    print("""Dit moet kloppen! Alles brandstof wordt nu in de tank geladen! """)

    while True: 
      lanceren = input("De raket is klaar om te lanceren! Kies:'LAUNCH' om te lanceren of kies: 'ABORT' om de lancering af te lassen! ").lower()
      if lanceren == "launch": 
          break
      elif lanceren == "abort":
          print("De missie om de laatste mensen te redden if afgelast... iedereen zijn vrijheid zal worden ingenomen...")
          print(game_over)
          exit()
      else: 
          print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
    
  else:
    print('''Ik heb mijn twijfels over de berekening.... maar we moeten het proberen.... !!!
    alle voorbereidingen zijn gedaan, iederen aanwezig op hun plaatsten en we wachten op de countdown.... via een buitencamera zien we de raket
    op een monitor en iedereen wacht in spannig af....''')
    print(launch_abort)
    flying = False
#########################################################################################################################################################################################################################################
def aftellen10():
  x = 11
  while x >0:
    x= x-1
    time.sleep(1)
    print(x)
  print("liftoff")
#########################################################################################################################################################################################################################################
def aftellenkort():
  x = 11
  while x >0:
    x= x-1
    time.sleep(1)
    print(x)
#########################################################################################################################################################################################################################################
def kijken_uit_raam():
  kijken_uit_raam = 0                                            
  while kijken_uit_raam >= 0:                                   
    vraag_kijken = input("Wilt u naar buiten kijken?")
    if vraag_kijken == "ja":
        kijken_uit_raam = +10
    if vraag_kijken == "nee":
        kijken_uit_raam = -10
    if kijken_uit_raam >5:
            print (kijken)
            break
    elif kijken_uit_raam <0:
            print("Ook goed, we gaan door")
            break
    else:
            print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")


######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################
#                                                                                              !!!ART FOR GAME ALL DOWN BELOW!!!
######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################
intro =("""
 ██╗░██████╗██████╗░░█████╗░░█████╗░███████╗  ░█████╗░██████╗░██████╗░██╗████████╗██╗░░░██╗██╗
 ╚█║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝╚█║
 ░╚╝╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░╚████╔╝░░╚╝
 ░░░░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░░╚██╔╝░░░░░
 ░░░██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗  ╚█████╔╝██████╔╝██████╔╝██║░░░██║░░░░░░██║░░░░░░
 ░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝  ░╚════╝░╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░
 """)

game_over = ("""
        
    ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░░░░░░░
    ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░░░░
    ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░░
    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░░
    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗██╗██╗
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝╚═╝""")

lift_off =('''

    ██╗░░░░░██╗███████╗████████╗░█████╗░███████╗███████╗
    ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
    ██║░░░░░██║█████╗░░░░░██║░░░██║░░██║█████╗░░█████╗░░
    ██║░░░░░██║██╔══╝░░░░░██║░░░██║░░██║██╔══╝░░██╔══╝░░
    ███████╗██║██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░
    ╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░░░░░''')

launch_abort = ("""

            ██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗  ░░░░██╗  ░█████╗░██████╗░░█████╗░██████╗░████████╗
            ██║░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║  ░░░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
            ██║░░░░░███████║██║░░░██║██╔██╗██║██║░░╚═╝███████║  ░░██╔╝░  ███████║██████╦╝██║░░██║██████╔╝░░░██║░░░
            ██║░░░░░██╔══██║██║░░░██║██║╚████║██║░░██╗██╔══██║  ░██╔╝░░  ██╔══██║██╔══██╗██║░░██║██╔══██╗░░░██║░░░
            ███████╗██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║  ██╔╝░░░  ██║░░██║██████╦╝╚█████╔╝██║░░██║░░░██║░░░
            ╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░  ╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
            """)
  
explosie =("""       ________________
                ____/ (  (    )   )  \___
                /( (  (  )   _    ))  )   )\ 
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
        ((__)        \\||lll|l||///          \_))
                    (   /(/ (  )  ) )\   )
                (    ( ( ( | | ) ) )\   )
                (   /(| / ( )) ) ) )) )
                (     ( ((((_(|)_)))))     )
                (      ||\(|(|)|/||     )
                (        |(||(||)||||        )
                (     //|/l|||)|\\ \     )
                (/ / //  /|//||||\\  \ \  \ _)
                """)

control = (""")-
          __________            .
      ____/,    _____)          .
      \  //    /   /            .
      _\/_     \  (             .
     /    \  ___\_|_            .
____/    \_\/       \           .
      (\___/\\       \          .
       |     \_______/          .
       |     //      \          .
   /   |     \_______/          .
___\   |   _//     \            .
    \__|  //\______/            .
       |__\______/  ____        .
    _____|____|____|____|       .
   /          __________ \      .
  /          /            \     .
  \_________/_____________/     .
                            """)

obsver =("""
                                       _..-,--.._
                                 ,`. ,',','      `.
                                 `. `,/`/          \ 
                                   :'.`:            :
        ____ _          _ __       | |`|            |
      _(    `.)        ( (  )`.    : `-'            ;     _
     ( (    ) ))      ( (    ))    ,\_            _/.  (`','
    ( (   )  _)        `-(__.'    '.  ```------'''  .`
     '.__)--'       .-..           |``-...____...-''|       
                   (_)_))          |                |         
              ,'`.        ___...---|                |--..._   
  ,'`. ,'`. ,'   _`.---'''         |                | "
-'..._`.   `.   /`-._  "      "    |    _           |       
       ```-..`./:::::)             `-...||______...-'    "   
              /:::_.'     "        "                "
           _.:.'''   "                       "              
           """)

komeet =('''

         ___---___                    
      .--          --.      
    ./   ()      .-.   \.
   /   o    .   (   )    \ 
  / .            '-'      \         
 | ()    .  O         .    |      
|                           |      
|    o            ()         |
|       .--.          O     |            
 | .   |    |              |
  \    `.__.'    o   .    /    
   \                     /                   
    `\  o    ()        /'    
      `--___   ___ --'
            ---
''')
raket = ("""
                            /\                
                           /  \              
                          /\/\/\              
                         /  ()  \             
                       /  //      \           
                      |  // /\     |          
                      |    /  \    |          
                      |   /    \   |          
                      |  | (  ) |  |          
                      |  | (  ) |  |          
                      |  |      |  |   /\     
                /--\  |  |  //  |  |  /  \    
               |----| |  | //   |  | |----|   
               |==  | | /|   .  |\ | |    |   
               | == | /  |   .  |  \ |    |   
               |    /    |   .  |    \    |   
               |  /  //  |   .  | ===  \  |   
               |/  ////  |   .  |     \\ \|   
              /   NA//   |   .  |  NASA \\ \  
             (           |      |  ==   //  ) 
               |    | |--|      |--| |    |   
                /  \     /  \/  \     /  \     
                ^^^^^    ^^^^^^^^    ^^^^^
                 ^^^       ^^^^       ^^^
                  ^         ^^         ^
""")

mars = ("""
              __...----...__
           .-' -=;::;::`;:::`-.
        .-'"; `-;:"";`-;   ,;;'`-.
      .''";;:     ,..   `.;;. .';;'.
     /  ,;;::,     `--'  ,.;: ::  .;:\ 
    ..- .; ;:,;,,.,   ,  ;;: ::;;:..;:.
   ;   ;    .;::,    ;:.;:::::::::;., ;
   |;. :      ;:;       `-;:::::-'""  |
   | ;,'  ,;::     ;.     `-;::  `;:::|
   ;`-;.   ,;:  ,;; `.  ."";,     ;;, ;
   '. ."".,        "".    ,;:;  '.,;::.
    `.                              .'
      `.                          .'
        `-.                    .-'
           ""--...______...--""
""")

looking_up =("""
  *    .  *       .   ,          *
           .       . .        *
 *   .   .'    * ,      .       .  ,     *
   .     *     .'
   '     .     .  *        *  .'.
       .   ' '        .    .    '   .
.  *        ,   *               '      *
                             .
         *          .   *


                  .
                 ( \ 
                 \  .     `{{{{}}  
                  \( \     ).  c
                   \  .     _  /
                    \( \ m/  _\\__
                     \  V/\`\ ++ /|
                      \( \ \ \__/ |
                     o/\_Z  \_____)
                     /=\.   .~~~~~|
                    // \\   |_____|
                   //   \\  | | | |
                  //     \\ | | | |
                 //      .\\( | ( |
                //         \\ | | |
               //          .\\| | |
              //           _|\\_| |
             //           (___\\__)
           .//                 \\
            """)

kijken = ("""
                        .              +   .             .   . .     .  .
                                .                    .       .     *
                .       *    . . . .  .   .  + .     .    .        .  .
                            .      .   .  +  . . .  .    .   .
                .                   .  .   .    .    . .       .      .
                                .     .     . +.    +  .
                        *         .              .       .   . .
                        . .                  .    * . . .  .  +   .
                        +      .           .   .      +        . 
                                            .       . +  .+. .
                .                      .     . + .  . .     .      .
                        .      .    .     . .       .   .    .       
                    *    .    . .  +    .  .       .  .   .    - O -
                        .     .                        .     .      *
                .      .   . .   .   .   . .  +   .    .            +
                """)

end_of_game = ('''

███████╗███╗░░██╗██████╗░  ░█████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝████╗░██║██╔══██╗  ██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
█████╗░░██╔██╗██║██║░░██║  ██║░░██║█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
██╔══╝░░██║╚████║██║░░██║  ██║░░██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
███████╗██║░╚███║██████╔╝  ╚█████╔╝██║░░░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚══════╝╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚═╝░░░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
''')