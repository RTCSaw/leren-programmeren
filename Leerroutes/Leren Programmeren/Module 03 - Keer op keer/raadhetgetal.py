from random import randint, random
import time
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Wat heb ik geleerd van deze opdracht?
# ik heb geleerd om te werken met functies, dat heb ik niet eerder gedaan. verder heb ik geleerd hoe abs werkt. die rekent het absolute verschil uit en dat is,,,
# heel erg handig om te weten. Verder vond ik het wel een leuke opracht die niet al te moeilijk was en goed is voor het niveau opbouwen.
score = 0

# extra funciton om gebruiker e helpen met het gokken voor hoger of lager.
def LagerOfHoger(getal ,target):
    if getal <= target:
        print("hoger")
    elif getal >= target:
        print("lager")


rondes = int(input("Hoeveel rondes wilt u spelen? "))
while rondes >= 21:
    print("u Kunt maximaal maar 20 rondes spelen. probeer het opnieuw")
    rondes = int(input("Hoeveel rondes wilt u spelen? "))

# deze line wordt ervoor gezorgt dat er niet meer dan het aantal ingevulde rondes wordt gespeeld.
aantal_rondes = 0
while rondes >= 1:
    print(f"Je hebt nog {rondes} rondes om te spelen")
    rondes -= 1
    geheimGetal = randint(1, 1000)

    # print(geheimGetal)  # hulpmiddel voor dev
    gokteller = 0
    while gokteller <= 9:
        inputGok = int(input("Welk getal denkt u dat het is? "))
        if inputGok == geheimGetal:
            print(f"Goed geraden! Het getal was {geheimGetal}! +1 punt")
            rondes -= 1
            score += 1
            aantal_rondes +=1
            volgende_ronde = input("wil je door naar de volgende ronde? ")
            # speler kan hier kiezen om door te gaan naar de volgende ronde.
            if volgende_ronde == "ja".lower():
                break
            else:
                time.sleep(3)  # spel wordt afgesloten als speler wilt stoppen.
                exit()

        # als de gok minder dan 50 van het te raden getal is dan kijkt de code bij line 46 tm 47 of het niet minder dan 20 is.
        elif abs(geheimGetal - inputGok) < 50:
            # als de gok wel meer dan 20 is van het te raden getal gaat de code door naar line 60
            if abs(geheimGetal - inputGok) < 20:
                print("heel warm")
                LagerOfHoger(inputGok, geheimGetal)
                gokteller += 1

            else:
                print("warm")

        elif abs(geheimGetal - inputGok) > 50:
            print("niet in de buurt")
            LagerOfHoger(inputGok, geheimGetal)
            gokteller += 1

        if gokteller >= 9:
            rondes -= 1
            print("u heeft 10 na 10x gokken het getal niet geraden. probeer het in de evt volgende ronde opnieuw!")
            aantal_rondes +=1
            break

# het spel is klaar
print(f"het spel is voorbij, u heeft in totaal {score} punten behaald in {aantal_rondes} rondes!")
