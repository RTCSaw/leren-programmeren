from FunctionsMars import *

print(intro)
time.sleep(1)
# Dit is de intro van het spel, hier wordt een korte samenvatting gegeven over het onderwerp.
delay_print('''Welkom bij Space Oddity!
In deze space game is de bedoeling dat mensen zo snel mogeljik de aarde verlaten wegens aanhoudende dreiging van aliens die de wereld willen overnemen
en mensen willen gebruiken als werkslaven. Er is 1 raket gebouwd met plek voor 1250 mensen!
Jij ben nu in leiding over de enige raket...
De laatste hoop voor de mensen aan boord... De laatste hoop voor de toekomst van de mensheid!''')
time.sleep(3)
delay_print('''Om van de grond af te komen hebben we natuurlijk vloeibare zuurstof nodig en brandstof.
Maar hoeveel is nog niet helemaal duidelijk...
Bereken hoeveel je nodig hebt in de volgende stage voor liftoff
LET OP! MAAK GEEN FOUTEN''')

time.sleep(2)
zuurstof()
launch()
aftellen10()
time.sleep(1)
latitude()
time.sleep(3)

delay_print("2 lange maanden later...")

time.sleep(3)
delay_print("""Onderweg naar Mars gaat er midden in de nacht ineens een hard alarm af... iedereen schrikt wakker en vraagt zich af wat er gebeurd.
de crew herkent het alarm en weet precies wat er aan de hand is. De crew haast zich naar de cockpit
Er zijn grote ruimtepuin stukken op onze route gedetecteerd vanaf een observatorium op aarde! Het observatorium stuurt een beeld naar de cockpit """)
time.sleep(2)
print(obsver)
time.sleep(1.5)
delay_print('laden van beeld....')
aftellenkort()
print(komeet)

delay_print ("""Dit is het stuk puin wat vanaf aarde is geobserveerd!
Ga snel achter de cockpit zitten en schiet de brokstukken met de lazers kapot!""")

komeetBattle() ##########################################################################################################

delay_print("""De rest van de reis lijkt rustig te verlopen, de mensen kijken rond via kleine raampjes naar buiten en zien de sterren. Sommige mensen hebben lol in de 0g kracht,
andere lezen ondersteboven een boek. Iedereen is vrij en blij. In de ramen is ook de planeet Mars te zien. Elke dag komt hij een stukje dichterbij en kan je de rode planeet steeds beter zien.
De grote kloven, bergen, oude rivierbedden en grote kale vlaktes...""") #verhaal
kijken_uit_raam()
time.sleep(3)
Alien_battle()       #################################################################################################
delay_print("De raket is zwaar beschadigd... we de raket vliegt op zijn laatste loodjes....")
time.sleep(2)
print(raket)

delay_print("Op het beeld is de beschadeging goed te zien....")
time.sleep(2)
delay_print("Na een lange en zware reis met veel tegenstoten zijn we eindelijk bij de planeet Mars aangekomen")
print(mars)
delay_print("""na een veilige landing is het eindelijk zo ver... we zijn vrij en we hoeven ons geen zorgen meer te maken
De aliens kunnen ons hier niet vinden. we sluiten ons aan bij de MarsColonyOne die al 20 jaar leeft op Mars... """)
print(looking_up)
print(end_of_game)