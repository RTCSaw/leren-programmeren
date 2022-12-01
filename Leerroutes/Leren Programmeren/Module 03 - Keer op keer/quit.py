
teller = 0
while True: 
    woord = input("Welk woord")
    if woord == "quit": 
        print(f"u heeft er {teller} pogingen over gedaan het juiste woord te raden")
        break    
    else: 
        print("Sorry, Dit is niet het juiste woord, probeer het opnieuw.")
        teller = teller +1

