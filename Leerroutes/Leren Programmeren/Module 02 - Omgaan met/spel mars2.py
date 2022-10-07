from msilib.schema import LaunchCondition
from re import X
from tracemalloc import stop
from termcolor import colored
import time
import sys
from ast import Pass, While
from random import randint

def delay_print(string):
    #print one character at a time
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

    
   
   #print one character at a time
def delay_input(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

######################################################################################################################################################

print('''

# ██╗░██████╗██████╗░░█████╗░░█████╗░███████╗  ░█████╗░██████╗░██████╗░██╗████████╗██╗░░░██╗██╗
# ╚█║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝╚█║
# ░╚╝╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░╚████╔╝░░╚╝
# ░░░░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░░╚██╔╝░░░░░
# ░░░██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗  ╚█████╔╝██████╔╝██████╔╝██║░░░██║░░░░░░██║░░░░░░
# ░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝  ░╚════╝░╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░
# ''')
time.sleep(2)

import random
#startup voor de startmotoren
num1zuurstof = random.randint(1,3)
num2brandstof = random.randint(1,5)

print('''Welkom bij Space Oddity!
In deze space game is de bedoeling dat mensen zo snel mogeljik de aarde verlaten wegens aanhoudende dreiging van aliens die de wereld willen overnemen
en mensen willen gebruiken als werkslaven. er is 1 raket gebouwd met plek voor 125000 mensen!
Jij ben nu in leiding over de enige raket... de laatste hoop voor de mensen aan boord... De laatste hoop voor de toekomst van de mensheid!''')
#tijd 12 seconde voor goede aansluit
time.sleep(3)
print()
print('''Om van de grond af te komen hebben we natuurlijk vloeibare zuurstof nodig en brandstof.
Maar hoeveel is nog niet helemaal duidelijk...
Bereken hoeveel je nodig hebt in de volgende stage voor liftoff''')
print()
time.sleep(2)

zuurstof = int(input (f'Het aantal liters in zuurstof: {num1zuurstof} + het aantal liters in brandstof {num2brandstof} is?'))
if int(zuurstof == (num1zuurstof + num2brandstof)):
 print("""Dat is helemaal juist! het juiste aantal liters zuurstof en brandstof wordt aan boord geladen! """)
elif print('''Ik heb mijn twijfels over de berekening.... maar we moeten het proberen.... !!!
alle voorbereidingen zijn gedaan, iederen aanwezig op hun plaatsten en we wachten op de countdown.... via een buitencamera zien we de raket
op een monitor en iedereen wacht in spannig af....'''):
   print("""

         ██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗  ░░░░██╗  ░█████╗░██████╗░░█████╗░██████╗░████████╗
         ██║░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║  ░░░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
         ██║░░░░░███████║██║░░░██║██╔██╗██║██║░░╚═╝███████║  ░░██╔╝░  ███████║██████╦╝██║░░██║██████╔╝░░░██║░░░
         ██║░░░░░██╔══██║██║░░░██║██║╚████║██║░░██╗██╔══██║  ░██╔╝░░  ██╔══██║██╔══██╗██║░░██║██╔══██╗░░░██║░░░
         ███████╗██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║  ██╔╝░░░  ██║░░██║██████╦╝╚█████╔╝██║░░██║░░░██║░░░
         ╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░  ╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
         """)

while True:
    lanceren = input("De raket is klaar om te lanceren! Als u de lancering wilt activeren kunt u dat doen doormiddel 'LAUNCH' or 'ABORT' ").lower()
    if lanceren == "launch":
        #  time.sleep(2)
        #  print('10')
        #  time.sleep(1)
        #  print('9')
        #  time.sleep(1)
        #  print('8')
        #  time.sleep(1)
        #  print('7')
        #  time.sleep(1)
        #  print('6')
        #  time.sleep(1)
        #  print('5')
        #  time.sleep(1)
        #  print('4')
        #  time.sleep(1)
        #  print('3')
        #  time.sleep(1)
        #  print('2')
        #  time.sleep(1)
        #  print('1')
        #  time.sleep(1)

         print('''


      ██╗░░░░░██╗███████╗████████╗░█████╗░███████╗███████╗
      ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
      ██║░░░░░██║█████╗░░░░░██║░░░██║░░██║█████╗░░█████╗░░
      ██║░░░░░██║██╔══╝░░░░░██║░░░██║░░██║██╔══╝░░██╔══╝░░
      ███████╗██║██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░
      ╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░░░░░''')
         break
    

    elif lanceren == "abort":
      delay_print("Je hebt er voor gekozen om niet te lanceren en gebruikt te worden als een werkslaaf.... iedereen die aan boord zit wacht op je om wraak te nemen....")
      print("""
               ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░░░░░░░
               ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░░░░
               ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░░
               ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░░
               ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗██╗██╗
               ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝╚═╝
                        """)
      break
    else:
        print("onbekende input, probeer het opnieuw ")

noordlat = random.randint(1,3)
eastlat = random.randint(1,5)
time.sleep(1)
keuze_koers = input("Om de raket op juiste koers moeten we een kant op sturen! Kies tussen'Kies tussen Links/Rechts'")
if keuze_koers == "links":
    print(""")-
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

print()
time.sleep(3)

print()
delay_print("2 lange maanden later...")
print()

time.sleep(3)
delay_print("""Onderweg naar Mars gaat er midden in de nacht ineens een hard alarm af... iedereen schrikt wakker en vraagt zich af wat er gebeurd.
de crew herkent het alarm en weet precies wat er aan de hand is. De crew haast zich naar de cockpit
Er zijn grote ruimtepuin stukken op onze route gedetecteerd vanaf een observatorium op aarde! Het observatorium stuurt een beeld naar de cockpit """)
time.sleep(2)
print("""
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
time.sleep(1.5)
print()
delay_print('laden van beeld....')
print()
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('''

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


delay_print ("""Dit is het stuk puin wat vanaf aarde is geobserveerd!
Ga snel achter de cockpit zitten en schiet de brokstukken met de lazers kapot!""")
print()

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
     print("er is iets fouts gedaan, probeer snel de lazers opnieuw te laden")


delay_print("""De rest van de reis lijkt rustig te verlopen, de mensen kijken rond via kleine raampjes naar buiten en zien de sterren. Sommige mensen hebben lol in de 0g kracht,
andere lezen ondersteboven een boek. Iedereen is vrij en blij. In de ramen is ook de planeet Mars te zien. Elke dag komt hij een stukje dichterbij en kan je de rode planeet steeds beter zien.
De grote kloven, bergen, oude rivierbedden en grote kale vlaktes...""") #verhaal


kijken_uit_raam = 0
while kijken_uit_raam >= 0:
            vraag_kijken = input("Wilt u naar buiten kijken?")
            if vraag_kijken == "ja":
                kijken_uit_raam = +10
            
            if vraag_kijken == "nee":
                kijken_uit_raam = -10
            
            if kijken_uit_raam >5:
                    print ("""
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
                    break
            elif kijken_uit_raam <0:
                    print("Ook goed, we gaan door")
                    break

            else:
                    print("Foute input, probeer het opnieuw")

    
time.sleep(3)
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
        print()
        #time.sleep(0.7)
        print("De aliens schieten teurg, ZET JE SCHRAP!!!")
        #time.sleep(1)
        print(f"De raket heeft nog ongeveer {raket_leven} hp over")
        
        if alien_leven <= 0:
          print("Je hebt de aliens een lesje geleerd!! We kunnen gelukkig veilig door!") 
        if raket_leven <= 0:
                print("De aliens hebben de raket kapot geschoten.... We zijn allemaal dood...")
                print("""
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░░░░░░░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░░░░
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗██╗██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝╚═╝
""")
                exit()
    
    else:
     print("er is iets fouts gedaan, probeer snel de lazers opnieuw te laden")
     raket_leven = raket_leven - alien_damage
     print(f"WE HEBBEN GEMIST EN WE ZIJN GERAAKT!!! WE HEBBEN NOG {raket_leven} hp over")

    
delay_print("De raket is zwaar beschadigd... we de raket vliegt op zijn laatste loodjes....")
time.sleep(2)
print("""
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

delay_print("Op het beeld is de beschadeging goed te zien....")
time.sleep(2)
print()