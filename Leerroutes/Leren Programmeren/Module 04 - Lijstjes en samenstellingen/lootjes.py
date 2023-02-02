import random
# de if controleerd voor een minimale input van 3
while True:
    aantal_deelnemers = int(input('Hoeveel namen wilt u toevoegen? : '))
    if aantal_deelnemers <3:
        print("u moet 3 of meer namen invullen")
    else:
        break
# input van namen, kijkt of de namen uniek zijn en voegt ze te toe aan de namen lijst.
namen = []
teller = 0 
while len(namen)< aantal_deelnemers:
    naam_input = input(f'Voeg de naam van deelnemer {teller + 1} toe: ')
    if naam_input not in namen:
        namen.append(naam_input)
        teller +=1 
    else:
        print(" deze namen zit al in de lijst...")
    
# hier wordt de namen lijstt geshuffeld
random.shuffle(namen)

#de zip functie pakt van de namen een index die is aangegeven, hierdoor zou nooit eigen naam getrokken worden.
koppels = zip(namen, namen[1:] + [namen[0]])

# Print uit de koppels
for gever, ontvanger in koppels:
    print(f'{gever} heeft {ontvanger} lootje ')