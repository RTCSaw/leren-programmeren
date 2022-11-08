from random import randint,random
import time
                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            #Wat heb ik geleerd van deze opdracht?
                            # ik heb geleerd om te werken met functies, dat heb ik niet eerder gedaan. verder heb ik geleerd hoe abs werkt. die rekent het absolute verschil uit en dat is,,,
                            # heel erg handig om te weten. Verder vond ik het wel een leuke opracht die niet al te moeilijk was en goed is voor het niveau opbouwen.

def LagerOfHoger():         #extra funciton om gebruiker e helpen met het gokken voor hoger of lager.
    if guess <= secretint:
        print("hoger")
    elif guess >= secretint:
        print("lager")

maxrondes= 20               #hier wordt de input van de gebruiker gevraagd voor hoeveel rondes de gebruiker wilt spelen
rondes = int(input("Hoeveel rondes wilt u spelen? "))

while rondes >= 21:
    print("u Kunt maximaal maar 20 rondes spelen. probeer het opnnieuw")
    rondes = int(input("Hoeveel rondes wilt u spelen? "))


while rondes >=1 or maxrondes <=0:              # deze line wordt ervoor gezorgt dat er niet meer dan het aantal ingevulde rondes wordt gespeeld.
    print(f"Je hebt nog {rondes} rondes om te spelen")
    maxrondes -= 1
    rondes -= 1
    randomNumber = randint(0,1000)

    score = 0
    gokteller = 0
    secretint = randint (1,1000)

    # print (secretint)             #hulpmiddel voor dev
    while gokteller <=9:
        guess = int(input("Welk getal denkt u dat het is? "))
        if guess == secretint:
            print(f"Goed geraden! Het getal was {secretint}! +1 punt")
            rondes -=1
            score +=1
            volgende_ronde = ("wil je door naar de volgende ronde? ")
            if volgende_ronde == "ja".lower:                #speler kan hier kiezen om door te gaan naar de volgende ronde.
                break
            else:
                    time.sleep(3)               #spel wordt afgesloten als speler wilt stoppen.
                    exit()
        
        elif abs (secretint - guess) <50:           # als de gok minder dan 50 van het te raden getal is dan kijkt de code bij line 46 tm 47 of het niet minder dan 2 is.
            if abs (secretint - guess)<20:          # als de gok wel meer dan 20 is van het te raden getal gaat de code door naar line 60
                print("heel warm")
                LagerOfHoger()
                gokteller +=1

            else:
                print("heet")

        elif abs (secretint - guess) <20:           # Code wordt hier getriggerrd als het gegokte getal minder dan 20 van het te raden getal is.
            print("heel warm")
            LagerOfHoger()
            gokteller +=1

        elif abs (secretint - guess) >50:
            print("niet in de buurt")
            LagerOfHoger()
            gokteller +=1
        
        if gokteller >=9:
            rondes -=1
            print("u heeft 10 na 10x gokken het getal niet geraden. probeer het in de evt volgende ronde opnieuw!")
            break
        
print(f"het spel is voorbij, u heeft in totaal {score} punten behaald!")            #het spel is klaar
