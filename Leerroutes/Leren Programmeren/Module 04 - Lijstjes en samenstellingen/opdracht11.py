from fruitmand import fruitmand

kleuren =[]                                                #lege list die later gevult wordt.                                    

for kleur in fruitmand:                              #hier worden alle kleuren toegevoegd aan de lege list kleuren.
    if kleur['color'] not in kleuren:
        kleuren.append(kleur['color'])

while True:
    kleur_input = (input("Welke kleur wil je? "))           # hier wordt de kleur gevraagd.
   
    if kleur_input in kleuren:
        print(f"Kleur {kleur_input} gekozen!")              # bevestiging dat kleur in de list zit en de kleur gekozen is.
        break
    else:
        print("voer een geldige kleur in! ")

rond, niet_rond, wel_rond = 0 , 0 , 0                       # Alle ronde tellers die bij houden hoeveel rond en niet rond is.

for x in range(len(fruitmand)):                             # for loop van de lengte van de fruitmand
    kleuren = fruitmand[x].get('color')                
    if kleuren == kleur_input:                              # als kleuren gelijk staat aan input kleur van gebruiker
        if fruitmand[x].get("round"):                       # als fruitmand [x] rond is, rond +1 wel rond +1
            rond +=1
            wel_rond +=1
        else:                                               # anders rond -1 niet rond -1
            rond -=1 
            niet_rond +=1

print(f" {niet_rond} niet rond, {wel_rond} wel rond")       #print de line met info