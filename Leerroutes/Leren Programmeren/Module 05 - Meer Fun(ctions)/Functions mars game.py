from random import randint
def battle_alien():
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

battle_alien()

def Alien_battle():
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
          time.sleep(1)
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
            