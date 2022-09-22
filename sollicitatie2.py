from asyncio import new_event_loop
from platform import java_ver


print('''Sollicitatie voor de vacature Ruimte vuilnis opruimer. In deze sollicatie
worden aan u vragen gesteld. u dient deze vragen eerlijk te antwoorden. mocht er een antwoord
niet naar waarheid ingevuld wordt, vervalt de sollicitatie''')
print("we bgeinnen met ja en nee vragen, beantwoord dus alleen met ja of nee! ")

soort_ervaring = (input('''Heeft u pratijks ervaring in 1 van de volgende beroepen?)
1: dieren dressuur
2: jongleren
3: acrobatiek
'''))

if soort_ervaring == "nee":
    pass

elif "ja":
 dieren_dressuur = int (input("hoeveel jaar ervaring heeft u met dierendressuur? "))
 jongleren = int (input("Hoeveel jaar ervaring heeft u met jongleren?"))
 acrobatiek = int (input("hoeveel jaar ervaring heeft u met acrobatiek? "))

 diploma = input("Bent u in bezit van een MBO diploma? ")
if diploma == "nee":
    pass

elif diploma == "ja":
    input ("Welk niveau MBO heeft u gedaan? ")


vrachtwagen_rijbewijs = input("bent u in bezit van een vrachtwagenbewijs?" )
if vrachtwagen_rijbewijs == "nee":
    pass

hoed = input("Bent u in bezit van een hoge hoed? ")
if hoed == "nee":
    pass

geslacht = input(" Wat is uw geslacht? (man/vrouw)")
if geslacht == "vrouw":
    print (input("Heeft u roodkrullend haar langer dan 20cm? "))
    if "nee":
        pass
elif geslacht == "man":
    print(input("Heeft een snor groter dan 10CM ? (ja/nee)"))
    if "nee":
        pass
    
lengte = int(input("Wat is uw lengt in CM? "))

gewicht = int(input("Wat is uw gewicht in KG? "))

certificaat = input("heeft u het certificaat: Overleven met gevaarlijk personeel?" )


sc1 = 0
sc2 = +1 
if dieren_dressuur >= 4:
    sc1 + sc2
    if jongleren >= 5:
        sc1 + sc2
        if acrobatiek >= 3:
            sc1 + sc2
if diploma == 4:
    sc1 + sc2 

if vrachtwagen_rijbewijs == "ja":
    sc1 + sc2

if hoed == "ja":
    sc1 + sc2

if geslacht == 'man' and "ja":
 sc1 + sc2

if geslacht == "vrouw" and "ja":
    sc1 + sc2

if lengte >= 150:
 sc1 + sc2

if gewicht >= 90:
    sc1 + sc2

if certificaat == "ja":
    sc1 + sc2

if sc1 == 5:
    print("U bent aangenomen! gefeliciteerd manneke")

if sc1 <= 8:
    print("U bent helaas niet aangekomen")







    

