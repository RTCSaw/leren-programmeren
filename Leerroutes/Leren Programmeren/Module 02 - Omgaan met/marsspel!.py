import time
import sys
from ast import Pass, While
from random import randint
import random

# hier vind je de functie die er voor zorgt daat le dalay_print kan gebruiken. Dit zorgt ervoor dat de tekst character voor character wordt uitgetypt.
# Dit geeft een game effect.
def delay_print(string):
    for char in string:
        sys.stdout.write(char)     
        sys.stdout.flush()
        time.sleep(0.03)

   #print one character at a time
def delay_input(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

print('''

██╗░██████╗██████╗░░█████╗░░█████╗░███████╗  ░█████╗░██████╗░██████╗░██╗████████╗██╗░░░██╗██╗
╚█║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║╚══██╔══╝╚██╗░██╔╝╚█║
░╚╝╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░╚████╔╝░░╚╝
░░░░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░  ██║░░██║██║░░██║██║░░██║██║░░░██║░░░░░╚██╔╝░░░░░
░░░██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗  ╚█████╔╝██████╔╝██████╔╝██║░░░██║░░░░░░██║░░░░░░
░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝  ░╚════╝░╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░
''')
time.sleep(2)
# Dit is de intro van het spel, hier wordt een korte samenvatting gegeven over het onderwerp.
delay_print('''Welkom bij Space Oddity!
In deze space game is de bedoeling dat mensen zo snel mogeljik de aarde verlaten wegens aanhoudende dreiging van aliens die de wereld willen overnemen
en mensen willen gebruiken als werkslaven. Er is 1 raket gebouwd met plek voor 1250 mensen!
Jij ben nu in leiding over de enige raket...
De laatste hoop voor de mensen aan boord... De laatste hoop voor de toekomst van de mensheid!''')
time.sleep(3)
print()
delay_print('''Om van de grond af te komen hebben we natuurlijk vloeibare zuurstof nodig en brandstof.
Maar hoeveel is nog niet helemaal duidelijk...
Bereken hoeveel je nodig hebt in de volgende stage voor liftoff
LET OP! MAAK GEEN FOUTEN''')
print()
time.sleep(2)
# De code hieronder zorgt ervoor dat ellke keer als je het spel laadt, er een andere som is. random.randint betekend letterlijk random,random int(getal)
num1zuurstof = random.randint(1,3)
num2brandstof = random.randint(1,5)
# Hier zorgt de while True ervoor dat als er een verkeerde input is de code zich weer terug pakt bij het begin. zo zorgt een verkeerde input van de gerbuiker
# niet direct voor een error. De while wordt stopgezet door de break. Dit zelfde geld voor de code op lijn 69 tot en met 85
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
            print("""
            
        ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░░░░░░░
        ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░░░░
        ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░░
        ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░░
        ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗██╗██╗
        ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝╚═╝""")
            exit()
        else: 
            print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")


    time.sleep(2)
    print('10')
    time.sleep(1)
    print('9')
    time.sleep(1)
    print('8')
    time.sleep(1)
    print('7')
    time.sleep(1)
    print('6')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('''


            ██╗░░░░░██╗███████╗████████╗░█████╗░███████╗███████╗
            ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
            ██║░░░░░██║█████╗░░░░░██║░░░██║░░██║█████╗░░█████╗░░
            ██║░░░░░██║██╔══╝░░░░░██║░░░██║░░██║██╔══╝░░██╔══╝░░
            ███████╗██║██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░
            ╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░░░░░
            ''')    
    flying = True       
                    
                
else:
    print('''Ik heb mijn twijfels over de berekening.... maar we moeten het proberen.... !!!
    alle voorbereidingen zijn gedaan, iederen aanwezig op hun plaatsten en we wachten op de countdown.... via een buitencamera zien we de raket
    op een monitor en iedereen wacht in spannig af....''')
    print("""

            ██╗░░░░░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗  ░░░░██╗  ░█████╗░██████╗░░█████╗░██████╗░████████╗
            ██║░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║  ░░░██╔╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
            ██║░░░░░███████║██║░░░██║██╔██╗██║██║░░╚═╝███████║  ░░██╔╝░  ███████║██████╦╝██║░░██║██████╔╝░░░██║░░░
            ██║░░░░░██╔══██║██║░░░██║██║╚████║██║░░██╗██╔══██║  ░██╔╝░░  ██╔══██║██╔══██╗██║░░██║██╔══██╗░░░██║░░░
            ███████╗██║░░██║╚██████╔╝██║░╚███║╚█████╔╝██║░░██║  ██╔╝░░░  ██║░░██║██████╦╝╚█████╔╝██║░░██║░░░██║░░░
            ╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░  ╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
            """)
    flying = False


    while True: 
        lanceren = input("De raket is klaar om te lanceren! Als u de lancering wilt activeren kunt u dat doen doormiddell 'LAUNCH' ").lower()
        if lanceren == "launch": 
            break
        elif lanceren == "abort":
            print("De missie om de laatste mensen te redden if afgelast... iedereen zijn vrijheid zal worden ingenomen...")
            print("""
            
        ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░░░░░░░
        ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░░░░░░░
        ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░░░░░░░
        ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░░░░░░░
        ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗██╗██╗
        ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝╚═╝╚═╝""")
            exit()
        else: 
            print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")

    time.sleep(2)

    teller = 10
    while teller > 0:
        print(teller)
        time.sleep(1)
        teller = teller -1

    
    print('''


    ██╗░░░░░██╗███████╗████████╗░█████╗░███████╗███████╗
    ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝
    ██║░░░░░██║█████╗░░░░░██║░░░██║░░██║█████╗░░█████╗░░
    ██║░░░░░██║██╔══╝░░░░░██║░░░██║░░██║██╔══╝░░██╔══╝░░
    ███████╗██║██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░
    ╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░░░░░''')

    print("ER GAAT EEN ALARM AF OP HET DASHBORD!!! HOUSTEN WE GOT A PROBLEM!! 'MASTER WARNING, MASTER WARNING, MASTER WARNING")
    print("""        ________________
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
    print("De raket is ontploft, iedereen aan boord is gesneuveld....")
    exit() #de exit zorgt er hier voor dat het spel is afgelopen. De computer zal bij een exit compleet uit de code stappen en de code stoppen met runnen.

#deze code is eerder uitgelegt bij line 11/12
noordlat = random.randint(1,3)
eastlat = random.randint(1,5)
time.sleep(1)
keuze_koers = input("Om de raket op juiste koers moeten we een kant op sturen! Kies tussen'Kies tussen Links/Rechts' ")
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
    time.sleep(1)
    delay_print("De raket is in een juiste baan op weg naar Mars, blijf deze kant op gaan! ")
    time.sleep(2)

#De try zorgt ervoor dat als eerste line 248 wordt getest. als dit klopt gaat de code door met runnen. zoniet dan komt de except van te pas.
#evt een while True van maken zodat als er een verkeerde input is de code weer naar try wordt gezet
    delay_print("Een enorme windstoot heeft de raket op een andere koers gebracht! Stuur zo snel mogelijk bij na het berekenen van de nieuwe koers!")
    print()
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

#storyline

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
                            #rots heeft een waarde van 20. de waarde is eigenlijk een soort health system
rots = 20

while rots > 0:
    playerinput = input("""vuur ZO SNEL MOGELIJK op de komeet!!
     Type vuur om de lazers te schieten!""")                    #hier kan de command vuur worden aangegeven. als dat gebeurd dan.. lees verder beneden.
    damage = randint(1,6)
    if playerinput == "vuur":                                   # dan gebeurd het volgende. rots = rots (20) - damage (randint1,6)
        rots = rots - damage                                    # dat betekend dat er random een damage wordt gedaan tussen 1 en 6 met aftrek van de rots (20)
        print(f"de rots heeft geschat nog {rots} hp over")
                                                                #line 346 geeft aan hoeveel hp de rots nog heeft.
        if rots <= 0:
          print("Je hebt de komeet kapot geschoten!! we kunnen gelukkig veilig door!") #dze line geeft aan dat als de rots minder dan een score heeft van 0 de print command wordt uitgegeven

    else:
     print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")


delay_print("""De rest van de reis lijkt rustig te verlopen, de mensen kijken rond via kleine raampjes naar buiten en zien de sterren. Sommige mensen hebben lol in de 0g kracht,
andere lezen ondersteboven een boek. Iedereen is vrij en blij. In de ramen is ook de planeet Mars te zien. Elke dag komt hij een stukje dichterbij en kan je de rode planeet steeds beter zien.
De grote kloven, bergen, oude rivierbedden en grote kale vlaktes...""") #verhaal


kijken_uit_raam = 0                                             #hier heb ik nog een extra score systeem gemaakt om te demonstreren dat ik dat begrijp en zelf kan maken.
while kijken_uit_raam >= 0:                                     #simpel maar wel handing
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
                    print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")

    
time.sleep(3)
alien_leven = 20
raket_leven = 30
delay_print("""ER IS EEN ALIEN ONS ACHTERVOLGT!! Ga de battle aan!""")

while alien_leven > 0:
    playerinput = input("""VUUR ZO SNEL MOGELIJK op de Aliens!!!""")            # Battle system zelfde als komeet battle, met toevoeging van hp system van de raket.
    damage = randint(1,6)               
    alien_damage = randint(1,6)
    if playerinput == "vuur":
        alien_leven = alien_leven - damage
        raket_leven = raket_leven - alien_damage
        print(f"de Aliens heeft geschat nog {alien_leven} hp over")
        print()
        time.sleep(0.7)
        print("De aliens schieten teurg, ZET JE SCHRAP!!!")
        time.sleep(0.7)
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
     print("Sorry, Dit begreep de computer niet, probeer het opnieuw.")
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
delay_print("Na een lange en zware reis met veel tegenstoten zijn we eindelijk bij de planeet Mars aangekomen")
print("""
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
delay_print("""na een veilige landing is het eindelijk zo ver... we zijn vrij en we hoeven ons geen zorgen meer te maken
De aliens kunnen ons hier niet vinden. we sluiten ons aan bij de MarsColonyOne die al 20 jaar leeft op Mars... """)
print("""
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
print('''

███████╗███╗░░██╗██████╗░  ░█████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝████╗░██║██╔══██╗  ██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
█████╗░░██╔██╗██║██║░░██║  ██║░░██║█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
██╔══╝░░██║╚████║██║░░██║  ██║░░██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
███████╗██║░╚███║██████╔╝  ╚█████╔╝██║░░░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚══════╝╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚═╝░░░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
''')