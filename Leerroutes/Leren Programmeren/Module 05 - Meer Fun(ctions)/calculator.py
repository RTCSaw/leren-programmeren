from functions import *   
firstRound = True
n1, n2 = False, False
while True:
    if firstRound :
        print("""
        Wat Wilt u Doen?
        A) Getallen optellen
        B) Getallen aftrekken
        C) Getallen vermedigvuldigen
        D) Getallen delen
        E) Getallen ophogen
        F) Getallen verlagen
        G) Getallen Verdubbelen
        H) Getallen Halveren
        STOP) de code zal stoppen
        Kies: """)

    else:
        print(f''' 
        Wat wil je met {n1} doen?
        A) getallen optellen?
        B) getallen aftrekken?
        C) getallen vermenigvuldigen?
        D) getallen delen?
        E) getal ophogen?
        F) getal verlagen?
        G) getal verdubbelen?
        H) getal halveren?
        ''')

    choice = input("Maak een keuze ").lower()
    if choice in  ("e","f"):
        n2 = 1
        
    elif choice in ("g", "h"):
        n2 = 2
    elif choice in ("q"):
        quit()

    if n1 == False:
        n1 = numberInput()
    if n2 == False:
        n2 = numberInput()

    if choice in ("a","e"):
        answer = optellen(n1,n2)
        operator = "+"

    if choice in ("b","f"):
        answer = aftrekken(n1,n2)
        operator = "-"

    if choice in ("c","g"):
        answer = keer(n1, n2)
        operator = "*"
    
    if choice in ("d", "h"):
        answer = delen(n1, n2)
        operator = "/"


    print(f"{n1} {operator} {n2} = {answer}")
    n1 = answer
    n2 = False
    firstRound = False